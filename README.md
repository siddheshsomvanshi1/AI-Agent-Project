## 🌸 LLaMA 3.2 AI Chatbot (React + Flask)

A professional **local AI chatbot** featuring a modern **React** frontend and a robust **Flask** backend, powered by the `llama3.2:latest` model via **Ollama**.
The app runs **fully offline** and features a clean, professional UI with formal color themes.

---

## 🚀 Features

*   🦙 **LLaMA 3.2** running locally via Ollama
*   ⚛️ **React Frontend**: Professional, responsive, and user-friendly interface
*   🐍 **Flask Backend**: Robust API handling chat streams
*   ⚡ **Streaming Responses**: Real-time typing effect
*   🎨 **Formal Design**: Clean aesthetics suitable for professional use
*   🔒 **Privacy**: No API keys, no internet required

---

## 📁 Project Structure

```
chatbot/
│
├── frontend/           # React Frontend Application
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── app.py              # Flask Backend API
├── requirements.txt    # Python Dependencies
├── lily.jpg            # Assets (Legacy)
└── README.md           # Documentation
```

---

## 🛠 Prerequisites

*   **Python 3.9+**
*   **Node.js & npm** (for the frontend)
*   **Ollama** installed on your system

👉 Download Ollama: [https://ollama.com](https://ollama.com)

### 1️⃣ Setup Ollama (Required First)

Before running the app, you must set up the AI model.

1.  **Install Ollama** from the link above.
2.  Open your terminal/command prompt.
3.  **Pull the Model**: Run the following command to download the LLaMA 3.2 model:
    ```bash
    ollama pull llama3.2:latest
    ```
4.  **Verify Installation**:
    ```bash
    ollama list
    ```
    *You should see `llama3.2:latest` in the list.*
5.  **Keep Ollama Running**: Ensure the Ollama app is running in the background (check your system tray).

---

## 📦 Installation & Setup

### 2️⃣ Backend Setup (Python)

Create and activate a virtual environment:

```bash
python -m venv venv
```

**Windows:**
```powershell
venv\Scripts\activate
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Frontend Setup (React)

Navigate to the frontend directory:
```bash
cd frontend
```

Install Node dependencies:
```bash
npm install
```

---

## ▶ Run the Application

(Skip "Pull the Model" if you already did it in Step 1)

You need to run the backend and frontend in separate terminals.

### Terminal 1: Start Backend
Make sure your virtual environment is activated.
```bash
# From the project root
python app.py
```
*Backend runs on http://localhost:5000*

### Terminal 2: Start Frontend
```bash
# From the project root
cd frontend
npm run dev
```
*Frontend runs on http://localhost:5173*

Open your browser to the URL shown in Terminal 2 to chat!

---

## 🎨 Customization

You can customize the frontend styles in `frontend/src/index.css`.
The backend logic is located in `app.py`.
