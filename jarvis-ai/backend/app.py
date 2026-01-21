from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path

from backend.llm.local_llm import ask_llm
from backend.rag.ingest import load_knowledge

# -----------------------------
# App Initialization
# -----------------------------
app = FastAPI(title="Jarvis AI Backend")

# Load system prompt safely
SYSTEM_PROMPT_PATH = Path("backend/prompts/system.txt")
SYSTEM_PROMPT = SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")

# Load vector store once at startup
VECTOR_STORE = load_knowledge()

# -----------------------------
# Request Schema
# -----------------------------
class ChatRequest(BaseModel):
    message: str

# -----------------------------
# Chat Endpoint
# -----------------------------
@app.post("/chat")
def chat(req: ChatRequest):
    try:
        # 1. Retrieve relevant context
        context_chunks = VECTOR_STORE.search(req.message)

        # 2. STRICT RAG GUARD (no hallucinations)
        if not context_chunks:
            return {
                "response": "I do not have enough information to answer that."
            }

        context = "\n".join(context_chunks)

        # 3. Build final prompt
        final_prompt = f"""
{SYSTEM_PROMPT}

Context:
{context}

User Question:
{req.message}
""".strip()

        # 4. Call local LLM (Ollama)
        response = ask_llm(final_prompt)

        return {"response": response}

    except Exception as e:
        # Backend never crashes
        return {
            "response": f"Backend error: {str(e)}"
        }
