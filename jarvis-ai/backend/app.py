from fastapi import FastAPI
from pydantic import BaseModel
from backend.llm.mock_llm import ask_llm
from pathlib import Path

app = FastAPI(title="Jarvis AI Backend")

SYSTEM_PROMPT = Path("backend/prompts/system.txt").read_text()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    full_prompt = f"""
{SYSTEM_PROMPT}

User Question:
{req.message}
"""
    response = ask_llm(full_prompt)
    return {"response": response}
