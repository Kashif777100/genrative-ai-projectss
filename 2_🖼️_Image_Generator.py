import os, io, base64
import streamlit as st
from PIL import Image
try:
    from openai import OpenAI
except Exception:
    OpenAI = None

st.set_page_config(page_title="Image Generator", page_icon="🖼️")
st.title("🖼️ Image Generator")

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

prompt = st.text_area("Prompt", placeholder="A cute robot barista serving coffee in a cozy cafe, cinematic lighting")
size = st.selectbox("Size", ["1024x1024", "512x512", "256x256"], index=0)
quality = st.selectbox("Quality", ["high", "standard"], index=0)

generate = st.button("Generate Image")
client, err = get_openai_client()
if err:
    st.warning(err)

if generate:
    if not prompt.strip():
        st.warning("Please write a prompt.")
    elif not client:
        st.error("Client not initialized. Check API key and dependencies.")
    else:
        try:
            result = client.images.generate(
                model=st.session_state.get("image_model","gpt-image-1"),
                prompt=prompt,
                size=size,
                quality=quality,
                n=1,
            )
            b64 = result.data[0].b64_json
            img_bytes = base64.b64decode(b64)
            st.image(img_bytes, caption="Generated image", use_column_width=True)
            st.download_button("Download image.png", img_bytes, file_name="generated.png", mime="image/png")
        except Exception as e:
            st.error(f"Image generation error: {e}")

st.markdown("> Please follow content guidelines and avoid disallowed content.")
