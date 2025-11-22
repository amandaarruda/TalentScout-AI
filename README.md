# TalentScout AI

### **Agente de Recrutamento Inteligente** construído com Google Gemini, LangChain & Streamlit.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Stack](https://img.shields.io/badge/AI-Google%20Gemini-orange)
![Framework](https://img.shields.io/badge/Framework-LangChain-green)

## Sobre o Projeto

O **TalentScout AI** é uma aplicação de GenAI desenvolvida para otimizar a análise de compatibilidade entre candidatos e vagas. O sistema atua como um agente especialista que lê currículos (PDF), processa a descrição da vaga e utiliza LLMs para gerar um relatório técnico com pontuação de match (0-100%), análise de gaps e veredito.

Este projeto aplica prática de **Engenharia de Prompt** e integração de **APIs de LLM (Google GenAI)**.

## Tech Stack

* **Python 3.10+**
* **Google Gemini (2.5 Flash Lite):** Motor de inferência de alta performance e baixa latência.
* **LangChain:** Framework de orquestração e templates de prompt.
* **Streamlit:** Interface web interativa com design customizado (CSS).
* **PyPDF:** Extração de dados não estruturados.

## Funcionalidades

* **Leitura de PDF:** Processamento de documentos brutos.
* **Análise Semântica:** Avaliação contextual de skills (não apenas palavras-chave).
* **Relatórios Estruturados:** Output em Markdown com Score, Pontos Fortes e Atenção.
* **Interface Clean:** UI otimizada com CSS customizado para melhor experiência de uso.

## Como Rodar

1. Clone o repositório
2. Instale as dependências:
```
pip install -r requirements.txt
```
3. Execute a aplicação:
```
streamlit run app.py
```
4. Insira sua Google API Key na barra lateral e comece a usar!

## Demonstração
### Plataforma
<img width="1677" height="936" alt="image" src="https://github.com/user-attachments/assets/16300fec-8e05-4735-8d5f-96e767698b12" />
