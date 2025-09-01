import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
import os
import json
import streamlit as st
from io import BytesIO
from PIL import Image
try:
    from openai import OpenAI
except Exception:
    OpenAI = None

st.set_page_config(page_title="Generative AI Project", page_icon="✨", layout="centered")

# --- Sidebar ---
st.sidebar.title("⚙️ Settings")

def get_openai_client():
    api_key = st.session_state.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None, "No API key found. Paste your OpenAI API key in the sidebar."
    if OpenAI is None:
        return None, "OpenAI SDK missing. Check requirements install."
    try:
        client = OpenAI(api_key=api_key)
        return client, None
    except Exception as e:
        return None, f"Failed to init OpenAI client: {e}"

st.sidebar.subheader("API Key")
key_input = st.sidebar.text_input("OpenAI API Key (sk-...)", type="password")
if key_input:
    st.session_state["OPENAI_API_KEY"] = key_input

st.sidebar.markdown("---")
st.sidebar.subheader("Models")
chat_model = st.sidebar.text_input("Chat model", value="gpt-4o-mini")
image_model = st.sidebar.text_input("Image model", value="gpt-image-1")

st.sidebar.markdown("---")
st.sidebar.subheader("Generation Params")
temperature = st.sidebar.slider("Temperature", 0.0, 2.0, 0.7, 0.1)
max_tokens = st.sidebar.slider("Max tokens", 64, 2048, 512, 32)

st.sidebar.markdown("---")
st.sidebar.info("Tip: Add your key in **Settings → Secrets** when deploying to Streamlit Cloud.")

st.title("✨ Generative AI Project")
st.write("Use the pages in the sidebar (or below) to access **Chat Assistant** and **Image Generator**.")

st.page_link("pages/1_💬_Chat_Assistant.py", label="💬 Chat Assistant", icon="💬")
st.page_link("pages/2_🖼️_Image_Generator.py", label="🖼️ Image Generator", icon="🖼️")

st.markdown("— Built with Streamlit + OpenAI API")
