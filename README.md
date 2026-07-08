# 🧠 LEXIENT - AI Powered Second Brain System

<p align="center">
  <b>Transform Information into Knowledge</b><br>
  An intelligent knowledge management system that summarizes, organizes, and helps users retain information from multiple sources.
</p>

---

## 📖 Overview

LEXIENT is an AI-powered Second Brain System designed to simplify information management by converting content from various sources into concise, searchable, and reusable knowledge.

The system accepts content from text, PDF documents, audio files, and YouTube videos, generates AI-powered summaries, stores them in a centralized knowledge base, and presents them through an interactive timeline. Future enhancements include semantic search, flashcard generation, intelligent recall, and knowledge graph visualization.

---

## ✨ Features

### ✅ Current Features

* Text Summarization
* PDF Summarization
* Audio Summarization
* YouTube Video Summarization
* MongoDB Storage
* Timeline-Based Knowledge History
* RESTful FastAPI APIs
* Modular Project Architecture
* Logging & Exception Handling

### 🚀 Upcoming Features

* Keyword Extraction
* Semantic Search
* AI Reflection Prompts
* Flashcard Generation
* Question Generation
* Knowledge Recall System
* Embedding-Based Similarity Search
* Knowledge Graph
* JWT Authentication
* Personalized Recommendations

---

# 🏗 Project Architecture

```
                User Input
                    │
      ┌─────────────┼─────────────┐
      │             │             │
    Text           PDF          Audio
                                  │
                              Whisper
                                  │
                           Transcript Text
                                  │
             YouTube Transcript Extraction
                                  │
                     T5 Summarization Model
                                  │
                     Generated Summary
                                  │
                         MongoDB Storage
                                  │
                         Timeline Interface
                                  │
      Search • Flashcards • Recall • Knowledge Graph
```

---

# 📂 Project Structure

```
LEXIENT/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── core/
│   ├── utils/
│
├── frontend/
│   ├── html/
│   ├── css/
│   └── js/
│
├── models/
│
├── logs/
│
├── requirements.txt
│
└── README.md
```

---

# ⚙ Technology Stack

## Backend

* Python
* FastAPI
* Uvicorn

## AI & Machine Learning

* Hugging Face Transformers
* T5 Summarization Model
* Whisper Speech Recognition

## Database

* MongoDB

## Frontend

* HTML
* CSS
* JavaScript

## Utilities

* Pydantic
* Logging
* Python Typing
* Exception Handling

---

# 🚀 Workflow

```
Input
   │
   ▼
Content Extraction
(Text / PDF / Audio / YouTube)
   │
   ▼
AI Summarization (T5)
   │
   ▼
Save Summary
(MongoDB)
   │
   ▼
Timeline
   │
   ▼
Search & Learning
```

---

# 🔌 API Endpoints

| Method | Endpoint             | Description               |
| ------ | -------------------- | ------------------------- |
| POST   | `/summarize-text`    | Summarize plain text      |
| POST   | `/summarize-pdf`     | Summarize uploaded PDF    |
| POST   | `/summarize-audio`   | Summarize audio files     |
| POST   | `/summarize-youtube` | Summarize YouTube videos  |
| POST   | `/save-note`         | Save generated summary    |
| GET    | `/get-notes`         | Retrieve stored summaries |

---

# 💾 Database Schema

```json
{
  "user_id": "123",
  "type": "pdf",
  "input": "Original Content",
  "summary": "Generated Summary",
  "created_at": "Timestamp"
}
```

---

# 🛠 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/LEXIENT.git
cd LEXIENT
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run the Application

```bash
uvicorn app.main:app --reload
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 📅 Development Roadmap

## ✅ Phase 1 – Core MVP

* Text Summarization
* PDF Summarization
* Audio Summarization
* YouTube Summarization
* MongoDB Integration
* Timeline View

---

## 🚀 Phase 2 – Intelligence Layer

* Keyword Extraction
* Search Engine
* Reflection Prompts

---

## 🚀 Phase 3 – Learning System

* Flashcards
* Question Generation
* Recall System

---

## 🚀 Phase 4 – Advanced Intelligence

* Embeddings
* Semantic Search
* Cross-Linking
* Knowledge Graph

---

## 🚀 Phase 5 – Production Ready

* Authentication
* Improved UI/UX
* Deployment
* Performance Optimization

---

# 📌 Future Enhancements

* Multi-user support
* Personalized AI Assistant
* Cloud Deployment
* Mobile Application
* Offline Knowledge Storage
* AI Recommendations
* Smart Note Linking

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Madhavi** & **Oshank Agrawal**

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub to support its development.

