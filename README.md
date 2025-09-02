# 📰 AI News Agent

An AI-powered News Summarizer & Sentiment Analyzer Agent  
Built with **FastAPI**, **Streamlit**, **HuggingFace Transformers**, and **GNews API**.

---

## 🚀 Features
- 🔎 Fetch news based on **location**, **date range**, and **category**
- ✍️ **Custom query** option (e.g., "earthquake in Turkey")
- 🧠 **Summarization** using DistilBART
- 😊 **Sentiment analysis** with emoji indicators
- 💬 Interactive **chat-like UI** (Streamlit)
- ⏳ Loading spinner for smooth UX
- 📅 Supports multiple date ranges

---

## 📂 Project Structure
- `backend.py` → FastAPI backend (fetch news, summarize, sentiment)
- `app.py` → Streamlit frontend (UI & chat interface)
- `requirements.txt` → Dependencies
- `report/` → Full project report (Word/PDF)
- `screenshots/` → Example UI screenshots

---

## ⚙️ Installation
```bash
# Clone repo
git clone https://github.com/Guptha815/AI-NEWS-AGENT.git
cd AI-NEWS-AGENT

# Create virtual env
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)

# Install dependencies
pip install -r requirements.txt
