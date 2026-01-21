from pathlib import Path
from backend.rag.vector_store import VectorStore


def load_knowledge():
    data = Path("data/sample_docs.txt").read_text().split("\n")
    store = VectorStore()
    store.add_documents(data)
    return store
