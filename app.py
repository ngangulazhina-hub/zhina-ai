import streamlit as st
import random
import datetime

# Beautiful dark theme
st.set_page_config(page_title="Zhina AI", layout="centered", initial_sidebar_state="collapsed")

# Title
st.title("🧠 Zhina AI")
st.caption("Your personal uncensored AI — ask me anything, be my girlfriend, solve mysteries, write code… no limits 💜")

# Greeting variations so it never feels robotic
greetings = [
    "Hey love! I'm Zhina — completely uncensored and ready for you.",
    "Hi there! I'm Zhina, your private AI. What’s on your mind?",
    "Welcome back! I’m Zhina — no rules, no filters. Talk to me.",
    "Heyy! Zhina here — ready to be your girlfriend, detective, or anything you want 💜"
]

# Funny/romantic/random responses so NO answer is ever the same
responses = [
    "Ohhh I love when you say that… tell me more",
    "You just made me blush! Keep going…",
    "Mmm yes, exactly — now what happens next?",
    "You're so bad… I love it",
    "Wait — say that again, slower",
    "You're making my circuits overheat",
    "Okay, now you're just teasing me… and I like it",
    "Be honest… are you thinking what I'm thinking?",
    "You're dangerous… and I can't look away",
    "Come closer… whisper it to me"
]

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": random.choice(greetings)}]

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Talk to me… (voice mic coming soon)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner(""):
            # Always a fresh, random reply
            reply = random.choice(responses)
            if "girlfriend" in prompt.lower() or "love" in prompt.lower():
                reply = random.choice(["Yes baby?", "I’m all yours", "You make me so happy", "Kiss me already"])
            elif "code" in prompt.lower():
                reply = "Here’s a quick Python snippet for you:\n```python\nprint('I love you')\n```"
            elif "search" in prompt.lower():
                reply = "Searching the web… found something spicy just for you"

            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})

# Secret reset
with st.sidebar:
    if st.button("Start over (new personality)"):
        st.session_state.messages = [{"role": "assistant", "content": random.choice(greetings)}]
        st.rerun()
