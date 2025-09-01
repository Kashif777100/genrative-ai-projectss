import os, json
import streamlit as st
try:
    from openai import OpenAI
except Exception:
    OpenAI = None

st.set_page_config(page_title="Chat Assistant", page_icon="💬")

st.title("💬 Chat Assistant")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "You are a helpful, concise assistant."}]

with st.expander("🧪 Quick Start Prompts"):
    st.write("- Explain a complex topic in simple terms")
    st.write("- Draft a professional email")
    st.write("- Brainstorm features for an app")

def get_openai_client():
    api_key = st.session_state.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None, "No API key. Set it in the main app sidebar."
    if OpenAI is None:
        return None, "OpenAI SDK missing. Run `pip install -r requirements.txt`"
    try:
        return OpenAI(api_key=api_key), None
    except Exception as e:
        return None, f"Client init error: {e}"

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_area("Your message", placeholder="Ask me anything...")
    submitted = st.form_submit_button("Send")
    if submitted and user_input.strip():
        st.session_state["messages"].append({"role": "user", "content": user_input})

client, err = get_openai_client()
if err:
    st.warning(err)

# Render chat
for msg in st.session_state["messages"]:
    with st.chat_message("assistant" if msg["role"]=="assistant" else "user"):
        st.markdown(msg["content"])

if client and len(st.session_state["messages"])>0 and st.session_state["messages"][-1]["role"]=="user":
    try:
        resp = client.chat.completions.create(
            model=st.session_state.get("chat_model","gpt-4o-mini"),
            messages=st.session_state["messages"],
            temperature=float(st.session_state.get("temperature",0.7)),
            max_tokens=int(st.session_state.get("max_tokens",512)),
        )
        assistant_text = resp.choices[0].message.content
        st.session_state["messages"].append({"role":"assistant","content":assistant_text})
        with st.chat_message("assistant"):
            st.markdown(assistant_text)
    except Exception as e:
        st.error(f"Generation error: {e}")

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    if st.button("🔄 Reset Chat"):
        st.session_state["messages"] = [{"role": "system", "content": "You are a helpful, concise assistant."}]
        st.experimental_rerun()
with col2:
    if st.button("⬇️ Export Chat as JSON"):
        data = json.dumps(st.session_state["messages"], indent=2)
        st.download_button("Download chat.json", data, "chat.json", "application/json")
