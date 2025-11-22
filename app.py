import streamlit as st
from pypdf import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os

st.set_page_config(page_title="TalentScout AI", layout="wide")

# Estilização
st.markdown("""
<style>
    /* Fundo Geral e Fontes */
    .stApp {
        background-color: #FFFFFF;
        color: #1E1E1E;
        font-family: 'Helvetica', sans-serif;
    }
    
    /* Títulos */
    h1, h2, h3 {
        color: #483D8B; /* Dark Slate Blue */
        font-weight: 700;
    }
    
    /* Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA;
        border-right: 1px solid #E0E0E0;
    }
    
    /* Botões */
    .stButton>button {
        background-color: #6C63FF; /* Lilás vibrante */
        color: white;
        border: none;
        border-radius: 8px;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #5a52d5;
        box-shadow: 0 4px 14px 0 rgba(108, 99, 255, 0.39);
    }
    
    /* Caixas de Texto e Upload */
    .stTextArea textarea {
        border: 1px solid #6C63FF;
        border-radius: 8px;
    }
    [data-testid="stFileUploader"] {
        border: 1px dashed #6C63FF;
        border-radius: 8px;
        padding: 10px;
    }
    
    /* Containers de Sucesso/Aviso */
    .stAlert {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def analyze_resume(resume_text, job_description, api_key):
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            api_key=api_key, 
            temperature=0.4
        )
        
        template = """
        Atue como um Recrutador Sênior.
        
        DESCRIÇÃO DA VAGA:
        {job_description}
        
        CURRÍCULO:
        {resume_text}
        
        Analise a compatibilidade e retorne APENAS um relatório técnico em Markdown (sem saudações) contendo:
        1. Match Score (0-100%)
        2. Pontos Fortes (Lista técnica)
        3. Gaps e Pontos de Atenção
        4. Veredito Final (Objetivo)
        """
        
        prompt = PromptTemplate(
            input_variables=["job_description", "resume_text"],
            template=template
        )
        
        chain = prompt | llm
        return chain.invoke({
            "job_description": job_description,
            "resume_text": resume_text
        }).content
        
    except Exception as e:
        return f"Erro técnico: {str(e)}"

# Sidebar
with st.sidebar:
    st.markdown("### Configuração")
    api_key = st.text_input("Google API Key", type="password", help="Sua chave do Google AI Studio")
    st.markdown("---")
    st.markdown("**Dica:** Cole sua chave aqui para habilitar a análise.")

# Cabeçalho
st.title("TalentScout AI")
st.markdown("##### Sistema de Análise de Compatibilidade Profissional")
st.markdown("---")

# Colunas Principais
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("Candidato")
    st.markdown("Faça o upload do currículo em PDF.")
    pdf_file = st.file_uploader("Upload do arquivo", type=["pdf"], label_visibility="collapsed")

with col2:
    st.subheader("Vaga")
    st.markdown("Cole a descrição completa da oportunidade.")
    job_desc = st.text_area("Descrição da Vaga", height=200, label_visibility="collapsed", placeholder="Cole aqui os requisitos...")

# Botão de Ação
st.markdown("<br>", unsafe_allow_html=True)
analyze_btn = st.button("INICIAR ANÁLISE DE COMPATIBILIDADE")

# Lógica de Execução
if analyze_btn:
    if not api_key:
        st.error("A API Key é obrigatória para processar a solicitação.")
    elif not pdf_file:
        st.error("Por favor, anexe o currículo do candidato.")
    elif not job_desc:
        st.error("Por favor, forneça a descrição da vaga.")
    else:
        with st.spinner("Processando análise com Gemini..."):
            try:
                raw_text = get_pdf_text([pdf_file])
                result = analyze_resume(raw_text, job_desc, api_key)
                
                # Exibição do Resultado
                st.markdown("---")
                st.subheader("Relatório de Análise")
                st.markdown(result)
                
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado: {e}")
