# Generative AI Project – Streamlit App

A clean, fully-working Streamlit project featuring:
- **AI Chat Assistant** (OpenAI `chat.completions` API)
- **Image Generator** (OpenAI `images.generate` API)
- API key entry via sidebar (not stored on server)
- Export/Download chat history
- Simple, certificate-ready structure and docs

## 1) Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL printed by Streamlit.

## 2) Provide your API key

- In the app sidebar, paste your **OpenAI API key** (sk-key...).  
- Or set it as an environment variable before running:
  - macOS/Linux: `export OPENAI_API_KEY="sk-..."`
  - Windows (PowerShell): `$env:OPENAI_API_KEY="sk-..."`

> The app prioritizes the sidebar key, then environment variable. It **does not** save your key to disk.

## 3) Deploy to Streamlit Community Cloud (to get a public share link)

1. Push this folder to a **new GitHub repo** (public or private).
2. Go to **share.streamlit.io** → **New app** → Select your repo & `app.py`.
3. Add a secret: `OPENAI_API_KEY="sk-..."` under **App settings → Secrets** (optional, you can also paste key in sidebar at runtime).
4. Click **Deploy**. You’ll get a public URL you can submit for certification.

## 4) Project structure

```
genai_project/
├─ app.py
├─ pages/
│  ├─ 1_💬_Chat_Assistant.py
│  └─ 2_🖼️_Image_Generator.py
├─ assets/
│  └─ sample_prompts.txt
├─ .streamlit/
│  └─ config.toml
├─ requirements.txt
├─ REPORT.md
└─ README.md
```

## 5) Notes

- Models: Defaults use `gpt-4o-mini` (chat) and `gpt-image-1` (images).  
  You can change these in the sidebar.
- Keep prompts safe and respectful. The app includes basic guardrails.
- **If your certification needs a short report**, see `REPORT.md`.
