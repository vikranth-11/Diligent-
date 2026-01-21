Jarvis — Local AI Assistant with RAG

Jarvis is a local, enterprise-oriented AI assistant built using a local large language model (Ollama) and Retrieval-Augmented Generation (RAG).
It answers user questions by retrieving relevant information from local documents and generating responses using a locally running language model.

Project Goals

This project is designed to be:

Fully local (no cloud APIs required)

Context-aware using vector search

ChatGPT-style conversational UI

Enterprise-focused and privacy-preserving

Key Features

Local LLM inference using Ollama (Mistral)

Retrieval-Augmented Generation (RAG) with FAISS

Semantic search using Sentence Transformers

FastAPI backend for inference and orchestration

Streamlit-based ChatGPT-style frontend

Multiple conversations with sidebar navigation

Explicit scope control via system prompt

All data remains on the local machine

How It Works

User enters a message in the Streamlit UI

UI sends a request to the FastAPI /chat endpoint

Backend retrieves relevant document chunks using FAISS

Retrieved context is combined with the system prompt

The final prompt is sent to the local LLM via Ollama

The generated response is returned and displayed in the UI

Setup Instructions
1. Prerequisites

Python 3.10 or higher

Git

Ollama installed

Install Ollama from:
https://ollama.com/download

2. Clone the Repository
git clone https://github.com/vikranth-11/Diligent-.git
cd Diligent/jarvis-ai

3. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate
# source venv/bin/activate  (Linux / macOS)

4. Install Dependencies
pip install -r requirements.txt

5. Pull the LLM Model
ollama pull mistral


Verify installation:

ollama run mistral

6. Start the Backend
uvicorn backend.app:app --reload


Backend URL: http://127.0.0.1:8000

API Docs: http://127.0.0.1:8000/docs

7. Start the Frontend

Open a new terminal:

streamlit run ui/app.py


UI URL: http://localhost:8501

Example Usage

In-scope questions:

What is the purpose of this assistant?

Explain the system behavior

Out-of-scope questions:

Teach me alphabets

Write a poem

The assistant clearly communicates scope limitations and may optionally provide general reference information depending on system prompt configuration.

Design Principles

Local-first architecture with no external APIs

Privacy-preserving by design

Scope-aware responses for enterprise use

Modular and extensible system design

Clear separation of UI, backend, and inference layers

Conclusion

Jarvis demonstrates a production-grade local AI assistant architecture using modern Retrieval-Augmented Generation techniques, local LLM inference, and a clean conversational interface, without relying on any cloud-based language model APIs.
