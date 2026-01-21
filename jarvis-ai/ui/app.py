import streamlit as st
import requests
import uuid

# -----------------------------
# Backend Config
# -----------------------------
BACKEND_URL = "http://127.0.0.1:8000/chat"

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Jarvis",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Initialize Session State
# -----------------------------
if "chats" not in st.session_state:
    first_chat_id = str(uuid.uuid4())
    st.session_state.chats = {
        first_chat_id: [
            {
                "role": "assistant",
                "content": "Hello! I’m **Jarvis**, your local AI assistant. How can I help you today?"
            }
        ]
    }
    st.session_state.active_chat_id = first_chat_id

# -----------------------------
# Sidebar (ChatGPT-style)
# -----------------------------
with st.sidebar:
    st.markdown("## 🤖 Jarvis")

    if st.button("➕ New chat", use_container_width=True):
        new_chat_id = str(uuid.uuid4())
        st.session_state.chats[new_chat_id] = [
            {
                "role": "assistant",
                "content": "New conversation started. How can I help?"
            }
        ]
        st.session_state.active_chat_id = new_chat_id

    st.divider()
    st.markdown("### Conversations")

    for idx, chat_id in enumerate(st.session_state.chats.keys(), start=1):
        if st.button(f"Chat {idx}", key=chat_id, use_container_width=True):
            st.session_state.active_chat_id = chat_id

    st.divider()
    st.markdown(
        """
        <p style="font-size:12px; color:gray;">
        🧠 Model: Local (Ollama – Mistral)<br>
        📦 Vector DB: FAISS<br>
        🔐 Data stays local
        </p>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Main Chat Area Header
# -----------------------------
st.markdown(
    """
    <h2 style="text-align:center;">🤖 Jarvis</h2>
    <p style="text-align:center; color:#94a3b8;">
        Local AI Assistant
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# Render Chat Messages
# -----------------------------
messages = st.session_state.chats[st.session_state.active_chat_id]

for msg in messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input("Message Jarvis…")

if user_input:
    # Show user message immediately
    messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend safely
    try:
        res = requests.post(
            BACKEND_URL,
            json={"message": user_input},
            timeout=30
        )
        res.raise_for_status()
        response_text = res.json().get("response", "⚠️ Empty response from backend.")

    except requests.exceptions.RequestException as e:
        response_text = f"⚠️ Backend error: {e}"

    # Show assistant response
    messages.append({"role": "assistant", "content": response_text})
    with st.chat_message("assistant"):
        st.markdown(response_text)
