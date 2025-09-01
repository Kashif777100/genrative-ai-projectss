# Project Report – Generative AI App (Streamlit)

## Abstract
This project demonstrates a production-ready Generative AI web application built with Streamlit. It contains two modules:
1) **Chat Assistant** powered by OpenAI chat completion models.
2) **Image Generator** powered by OpenAI image generation models.

It includes security-friendly API key handling, parameter controls (temperature, max tokens), history export, and instructions for one-click cloud deployment.

## Problem Statement
Learners often need a simple, reliable demo they can deploy quickly to showcase generative AI capabilities for certification or portfolio submissions.

## Objectives
- Provide a clean, minimal, and extensible codebase.
- Offer both text generation and image generation.
- Ensure easy deployment and reproducibility.

## System Architecture
- **UI:** Streamlit
- **Backend SDK:** OpenAI Python SDK
- **Models:** `gpt-4o-mini` for chat; `gpt-image-1` for images
- **State:** Streamlit session_state stores chat history locally during a session.
- **Security:** API key is read from sidebar or environment variables. Not persisted on disk.

## Features
- Chat with memory (session only)
- Adjustable temperature, max tokens
- Prompt templates for quick starts
- Export chat as JSON
- Generate images from text prompts; quality and size switches
- Download generated images

## Ethical Considerations
- Users are warned not to submit or request disallowed content.
- The app does not store user data server-side by default.
- Outputs can be inaccurate; user confirmation is recommended for critical tasks.

## How to Use
1. Provide your API key in the sidebar (or set as secret).
2. Choose a model in the sidebar.
3. Use the **Chat Assistant** page to converse and export results.
4. Use the **Image Generator** page to create images and download them.

## Results
The app successfully generates coherent text and high-quality images (subject to model capability and prompts).

## Future Work
- Add conversation persistence in a database
- Add other providers (e.g., Gemini, OpenRouter)
- Add RAG (document Q&A) with vector search

## References
- OpenAI API docs
- Streamlit docs
