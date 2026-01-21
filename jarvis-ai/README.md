🤖 Jarvis — Local AI Assistant with RAG

Jarvis is a local, enterprise-oriented AI assistant built using a local LLM (Ollama) and Retrieval-Augmented Generation (RAG).
It answers user questions by retrieving relevant information from local documents and generating responses using a locally running language model.

This project is designed to be:

🔐 Fully local (no cloud APIs required)

🧠 Context-aware using vector search

💬 ChatGPT-style UI

🏢 Enterprise-focused

✨ Key Features

Local LLM inference using Ollama (Mistral)

RAG pipeline with FAISS vector database

Semantic search using Sentence Transformers

FastAPI backend

Streamlit ChatGPT-style frontend

Multiple conversations with sidebar navigation

Clear scope control via system prompt

All data stays on your machine

🧱 Project Structure
jarvis-ai/
│
├── backend/
│ ├── app.py # FastAPI backend
│ │
│ ├── llm/
│ │ ├── mock_llm.py # Mock LLM (early development)
│ │ └── local_llm.py # Ollama integration (Mistral)
│ │
│ ├── rag/
│ │ ├── ingest.py # Document ingestion & indexing
│ │ └── vector_store.py # FAISS vector store
│ │
│ ├── prompts/
│ │ └── system.txt # System prompt (behavior control)
│ │
│ └── **init**.py
│
├── ui/
│ └── app.py # Streamlit UI (ChatGPT-style)
│
├── data/
│ └── sample_docs.txt # Knowledge base documents
│
├── requirements.txt
└── README.md

🏗️ Architecture Diagram
┌─────────────────────────────┐
│ Streamlit UI │
│ (ChatGPT-style frontend) │
│ ui/app.py │
└──────────────┬──────────────┘
│ HTTP (POST /chat)
▼
┌─────────────────────────────┐
│ FastAPI Backend │
│ backend/app.py │
│ │
│ ┌───────────────────────┐ │
│ │ System Prompt │ │
│ │ backend/prompts/ │ │
│ │ system.txt │ │
│ └───────────┬───────────┘ │
│ │ │
│ ┌───────────▼───────────┐ │
│ │ RAG Pipeline │ │
│ │ backend/rag/ │ │
│ │ - ingest.py │ │
│ │ - vector_store.py │ │
│ └───────────┬───────────┘ │
│ │ │
│ ┌───────────▼───────────┐ │
│ │ FAISS Vector Database │ │
│ │ (local, in-memory) │ │
│ └───────────┬───────────┘ │
│ │ │
│ ┌───────────▼───────────┐ │
│ │ Local LLM (Ollama) │ │
│ │ Model: Mistral │ │
│ │ backend/llm/local_llm │ │
│ └───────────────────────┘ │
└─────────────────────────────┘

🧠 How It Works (Flow)

User enters a message in the Streamlit UI

UI sends request to FastAPI /chat endpoint

Backend:

Retrieves relevant document chunks using FAISS

Injects context + system prompt into final prompt

Prompt is sent to Ollama (Mistral) running locally

Model generates a response

Response is returned and rendered in the UI

⚙️ Setup Instructions
1️⃣ Prerequisites

Python 3.10+

Git

Ollama installed

👉 Install Ollama:
https://ollama.com/download

2️⃣ Clone the Repository
git clone https://github.com/your-username/jarvis-ai.git
cd jarvis-ai

3️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate # Windows

# source venv/bin/activate # Linux / macOS

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Pull the LLM Model
ollama pull mistral

Verify:

ollama run mistral

6️⃣ Start the Backend
uvicorn backend.app:app --reload

Backend runs at:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

7️⃣ Start the UI

In a new terminal:

streamlit run ui/app.py

UI runs at:

http://localhost:8501

Example Queries

✅ In-scope:

“Explain our system architecture”

“What is the purpose of this assistant?”

⚠️ Out-of-scope:

“Teach me alphabets”

“Write a poem”

The assistant clearly communicates scope limitations and may optionally provide general reference information depending on prompt configuration.

🔐 Design Principles

Local-first: No external APIs

Privacy-preserving: Data never leaves the machine

Scope-aware: Optimized for enterprise knowledge use

Modular: LLM, RAG, UI are decoupled

Extensible: Easy to add new documents or models

🏁 Conclusion

Jarvis demonstrates a production-grade local AI assistant architecture using modern RAG techniques, local inference, and a polished chat UI — without relying on any cloud LLM APIs.
