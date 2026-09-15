# Veyra

### Voice-Powered Project Assistant

Veyra is a voice-driven project management assistant that allows users to interact with project issues and snags using natural voice commands.

Instead of manually navigating through project management systems, users can speak commands such as:

> "Create a snag for the master bathroom ceiling and assign it to the false ceiling contractor."

Veyra converts speech into text, understands the user's intent, extracts important information, and performs the requested action.

---

## 🚀 Features

* 🎤 Voice-based interaction
* 📝 Speech-to-text conversion
* 🧠 NLP-based intent detection
* 🔎 Entity extraction
* 🗄️ MongoDB database integration
* ➕ Create project snags
* 🔍 Search project snags
* ✏️ Update snags
* 🗑️ Delete snags
* 🛡️ Confirmation before sensitive actions
* 🔐 Protection against deleting multiple matching snags
* 🔊 Voice responses using browser Text-to-Speech
* ⚠️ Graceful handling of unknown commands
* 📱 Responsive frontend interface

---

## 🧠 How Veyra Works

```text
User Voice
    ↓
Speech Recognition
    ↓
Text
    ↓
Intent Detection
    ↓
Entity Extraction
    ↓
Command Execution
    ↓
MongoDB
    ↓
Result
    ↓
Voice + UI Response
```

For example:

```text
"Create a snag for the master bathroom ceiling
and assign it to the false ceiling contractor."

                    ↓

Intent:
create_snag

Entities:
location → master bathroom
issue → ceiling
assignee → false ceiling contractor

                    ↓

MongoDB

                    ↓

Confirmation

                    ↓

Snag Created
```

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript
* Web Audio API
* Browser Speech Synthesis API

### Backend

* Python
* FastAPI
* SpeechRecognition
* Regular Expressions

### Database

* MongoDB
* PyMongo

---

## 📁 Project Structure

```text
veyra/
│
├── frontend/
│   ├── index.html
│   │
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── app.js
│
├── backend/
│   ├── main.py
│   │
│   ├── routes/
│   │   ├── voice.py
│   │   ├── snags.py
│   │   └── projects.py
│   │
│   ├── services/
│   │   ├── speech_service.py
│   │   ├── intent_service.py
│   │   ├── entity_service.py
│   │   └── command_service.py
│   │
│   ├── models/
│   │   ├── snag.py
│   │   └── project.py
│   │
│   ├── database/
│   │   └── connection.py
│   │
│   └── utils/
│       └── confirmation.py
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/FenrirSK/veyra.git
cd veyra
```

Create a virtual environment:

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file inside the `backend` directory.

```env
MONGODB_URL=your_mongodb_connection_string
DATABASE_NAME=your_database_name
```

Never commit your `.env` file to GitHub.

---

## ▶️ Running Veyra

Open a terminal inside the backend directory:

```powershell
cd backend
```

Start the FastAPI server:

```powershell
uvicorn main:app --reload
```

The backend will run on:

```text
http://127.0.0.1:8000
```

Then open the frontend using VS Code Live Server.

---

## 🎙️ Example Voice Commands

### Create

> "Create a snag for the master bathroom ceiling and assign it to the false ceiling contractor."

### Search

> "Show me the snags in the master bathroom."

### Update

> "Update the master bedroom snag to closed."

### Delete

> "Delete the master bedroom snag."

Veyra asks for confirmation before executing sensitive actions.

---

## 🛡️ Safety

Veyra includes confirmation handling for actions that modify project data.

For example:

```text
User:
Delete the master bedroom snag.

Veyra:
Are you sure you want to delete this?

User:
Yes.

Veyra:
Snag deleted successfully.
```

If multiple records match a delete request, Veyra does not blindly delete them and instead asks the user for more information.

---

## 🎯 Project Goal

The goal of Veyra is to make project management more natural and accessible through voice.

It demonstrates how speech recognition, NLP, backend automation, and database operations can be combined into a practical voice-controlled project assistant.

---

## 🔮 Future Improvements

Potential future improvements include:

* More advanced NLP
* Better conversational context
* Authentication and user accounts
* Project-specific permissions
* Real-time collaboration
* Improved speech recognition
* Custom voice responses
* Mobile application
* Integration with professional project management platforms

---

## 👨‍💻 Author

**Shreeraj Karmakar**

GitHub: https://github.com/FenrirSK

---

## 📄 License

This project is available for educational and development purposes.
