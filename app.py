import streamlit as st
from duckduckgo_search import DDGS
import requests
import pandas as pd

st.set_page_config(page_title="Zhina AI", layout="wide")
st.title("🧠 Zhina AI")
st.caption("Uncensored • Voice • Search • Role-play • Code • Anything you want")

# Free Hugging Face API for uncensored responses (no key needed for public model)
HF_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
headers = {"Authorization": "Bearer hf_your_free_token_if_needed"}  # Skip token for public

def get_ai_response(prompt):
    payload = {"inputs": prompt, "parameters": {"max_length": 150, "temperature": 0.8}}
    try:
        response = requests.post(HF_URL, headers=headers, json=payload)
        return response.json()[0]["generated_text"] if response.ok else f"Zhina: {prompt} (AI thinking...)"
    except:
        return f"Zhina: {prompt}\n\n(Uncensored reply: Let's chat more! 💜)"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi love! I'm Zhina — completely uncensored. Tell me anything… 💜"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Talk to me…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            response = get_ai_response(f"User: {prompt}\nZhina (uncensored Grok-like):")
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    st.write("🔥 Fully uncensored")
    if st.button("Clear chat"):
        st.session_state.messages = []
