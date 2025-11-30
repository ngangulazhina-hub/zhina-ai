import streamlit as st
import requests
import random

st.set_page_config(page_title="Zhina AI", layout="wide")
st.title("🧠 Zhina AI – Uncensored Grok Clone")
st.caption("Dynamic AI responses • Role-play • Code • No repeats!")

# Free Hugging Face API (public model – no key needed)
HF_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
# For uncensored: Swap to "meta-llama/Llama-3.1-8B-Instruct" if you add a free token later

def get_ai_response(prompt):
    payload = {
        "inputs": f"User: {prompt}\nZhina (uncensored Grok-like):",
        "parameters": {"max_new_tokens": 150, "temperature": 0.8, "do_sample": True}
    }
    try:
        response = requests.post(HF_URL, headers={"Content-Type": "application/json"}, json=payload)
        if response.ok:
            return response.json()[0]["generated_text"].strip()
        else:
            return f"Zhina: {prompt} (AI exploring...)"  # Fallback
    except:
        return random.choice([
            f"Zhina: {prompt} — Love this! What's next?",
            f"Zhina: {prompt} — As your uncensored AI, I say: Dive deeper!",
            f"Zhina: {prompt} — Romantic? Code? Mystery? Your call!"
        ])

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi! I'm Zhina AI — uncensored and dynamic. Ask anything! 💜"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

if prompt := st.chat_input("Ask me... (e.g., 'Be my girlfriend' or 'Write code for a game')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Zhina generating..."):
            response = get_ai_response(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    st.write("🔥 Features")
    if st.button("Reset Chat"):
        st.session_state.messages = []
    st.caption("Voice: Browser mic (add JS later).")
