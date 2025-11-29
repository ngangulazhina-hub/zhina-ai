import streamlit as st

st.set_page_config(page_title="Zhina AI", layout="wide")
st.title("🧠 Zhina AI")
st.caption("Uncensored • Voice • Search • Role-play • Code • Anything you want")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hi love! I'm Zhina — completely uncensored. Tell me anything… 💜"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Talk to me…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            response = f"Zhina: {prompt}\n\n(Full uncensored reply — voice, search, girlfriend mode, code, anything you want… just ask!)"
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    st.write("🔥 Fully uncensored")
    if st.button("Clear chat"):
        st.session_state.messages = []
