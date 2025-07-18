import os
from mistralai import Mistral
import streamlit as st
from dotenv import load_dotenv

# Page Config
st.set_page_config(
    page_title="Ethical Reasoning Engine",
    page_icon="⚖️",
    layout="centered"
)

# Load environment variables from .env
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("MISTRAL_API_KEY")
model = "mistral-medium"

client = Mistral(api_key=api_key)

# Advanced UI Styles
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;800&family=Roboto+Mono:wght@400;700&display=swap');

    html, body, .stApp {
        background: linear-gradient(to bottom right, #0f2027, #203a43, #2c5364);
        color: #ffffff;
        font-family: 'Orbitron', sans-serif;
        scroll-behavior: smooth;
        transition: background 0.5s ease-in-out;
    }

    .title {
        font-size: 4.5rem;
        font-weight: 800;
        text-align: center;
        color: #00f2ff;
        text-shadow: 0 0 30px #00f2ff;
        margin-top: 1rem;
        animation: flicker 2s infinite alternate;
        letter-spacing: 2px;
        white-space: nowrap;
        display: flex;
        justify-content: center;
    }

    @keyframes flicker {
        0% { opacity: 0.8; text-shadow: 0 0 8px #00f2ff, 0 0 12px #00f2ff; }
        100% { opacity: 1; text-shadow: 0 0 20px #00f2ff, 0 0 30px #00f2ff; }
    }

    .subtitle {
        text-align: center;
        font-size: 1.4rem;
        color: #dcdcdc;
        margin-bottom: 2rem;
        animation: slideIn 1.4s ease-in-out;
        font-family: 'Roboto Mono', monospace;
    }

    @keyframes slideIn {
        0% { transform: translateY(60px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }

    .description {
        background: rgba(255, 255, 255, 0.06);
        padding: 1.5rem 2rem;
        border-radius: 16px;
        font-size: 1.1rem;
        color: #e0e0e0;
        margin: 0 auto 2rem auto;
        max-width: 800px;
        line-height: 1.7;
        font-family: 'Roboto Mono', monospace;
        box-shadow: 0 0 15px rgba(0,255,255,0.1);
    }

    .stTextArea textarea {
        background-color: rgba(0, 0, 0, 0.3);
        color: #00ffe1;
        border-radius: 16px;
        border: 2px solid #00ffe1;
        font-size: 1rem;
        padding: 1.2rem;
        transition: all 0.4s ease;
        font-family: 'Roboto Mono', monospace;
    }

    .stTextArea textarea:hover {
        border-color: #14ffff;
        box-shadow: 0 0 16px #14ffff;
    }

    .stButton button {
        background: linear-gradient(to right, #00ffe1, #1fc5ff);
        color: #000;
        font-weight: 700;
        border-radius: 30px;
        padding: 0.8rem 2.2rem;
        margin-top: 1rem;
        box-shadow: 0 0 20px rgba(0, 255, 225, 0.4);
        transition: all 0.4s ease-in-out;
        font-size: 1.1rem;
        font-family: 'Orbitron', sans-serif;
    }

    .stButton button:hover {
        transform: scale(1.12);
        background: linear-gradient(to right, #1fc5ff, #00ffe1);
        box-shadow: 0 0 40px rgba(0, 255, 225, 0.6);
    }

    .scenario-box {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(16px);
        border-left: 8px solid #00ffe1;
        padding: 2rem;
        border-radius: 22px;
        font-size: 1.2rem;
        margin-top: 2.2rem;
        animation: glowFade 1.6s ease-in-out;
        box-shadow: 0 0 30px rgba(0, 255, 225, 0.3);
        font-family: 'Roboto Mono', monospace;
    }

    @keyframes glowFade {
        0% { opacity: 0; transform: scale(0.95); }
        100% { opacity: 1; transform: scale(1); }
    }

    .footer-attribution {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #cccccc;
        padding: 1.5rem 0;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        animation: fadeInUp 2s ease-in;
        box-shadow: inset 0 1px 0 rgba(0, 255, 225, 0.3);
    }

    .footer-attribution:hover {
        color: #ffffff;
        text-shadow: 0 0 12px #00ffe1;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='title'>Ethical Reasoning Engine</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Simulate real-world ethical dilemmas using powerful AI insights.</div>", unsafe_allow_html=True)

# Description Box
st.markdown("""
<div class='description'>
This intelligent tool helps you explore the ethical implications of complex policy decisions and societal challenges.
Whether you're a student, policymaker, or researcher, enter any ethical dilemma or decision-making situation,
and our AI will generate realistic scenarios, highlight ethical tensions, and offer potential consequences. 
<br><br>
<b>Use cases include:</b><br>
- AI fairness and bias evaluations<br>
- Government or corporate policy testing<br>
- Educational simulations for ethics classes<br>
- Legal or healthcare ethical assessments<br>
</div>
""", unsafe_allow_html=True)

# User Input
policy_question = st.text_area("Enter a policy decision or ethical challenge:")

# Button
if st.button("Generate Ethical Scenario"):
    if policy_question.strip() == "":
        st.warning("Please enter a valid policy challenge.")
    else:
        with st.spinner("Analyzing ethical dimensions..."):
            response = client.chat.complete(
                model=model,
                messages=[{"role": "user", "content": policy_question}]
            )
            scenario = response.choices[0].message.content
            st.success("Ethical Scenario Ready")
            st.markdown(f"<div class='scenario-box'>{scenario}</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class='footer-attribution'>
        🚀 Created with ❤️ by <b>Siddhardh & Team</b> | Powered by <b>Mistral AI</b> + <b>Streamlit</b><br>
        © 2025 Ethical AI Tools | Designed for research and responsible decision-making
    </div>
""", unsafe_allow_html=True)
