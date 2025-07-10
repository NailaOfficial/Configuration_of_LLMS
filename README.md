# Configuration of LLMs with Gemini API 🌐🧠

This project demonstrates how to configure and run various **AI agents** using the **Gemini API** via the `openai-agents` library. The structure is modular, with three levels of configuration:

---

## 📁 Project Structure
Configuration_of_LLMS/
│
├── 1-Agent_Level_Configuration/
│ └── Parenting_Agent/
│ └── main.py
│
├── 2-Run_Level_Configuration/
│ └── Animal_Fun_Bot/
│ └── main.py
│
├── 3-Global_Level_Configuration/
│ └── Life_Advice_Guide/
│ └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 📌 Features

- ✅ Use of **Gemini (Google) API** with OpenAI-compatible syntax
- ✅ Custom agents with unique personalities:
  - 🧸 Parenting Assistant  
  - 🐾 Animal Quiz Coach  
  - 🌱 Life Advice Bot
- ✅ Full async/sync chat loops with user interaction
- ✅ `.env` based secure configuration

---

## 🔐 Environment Setup

Create a `.env` file in the root:

```env
GEMINI_API_KEY=your_api_key_here
🚀 How to Run
Create a virtual environment:

bash
Copy
Edit
python -m venv .venv
Activate it:

Windows:

bash
Copy
Edit
.venv\Scripts\activate
Mac/Linux:

bash
Copy
Edit
source .venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Go to any agent folder and run:

bash
Copy
Edit
python main.py
📦 Dependencies
python-dotenv

openai-agents

openai (used with Gemini base URL)

🛡 License
MIT License — for educational & personal use.

🤖 Author
Naila Ameer
Generated with ❤️ and LLMs

yaml
Copy
Edit

---

## 📌 Kya karna hai ab?

1. Apni project directory ke root mein ek new file banaye:

   📄 **`README.md`**

2. Upar wala **poora content copy kar ke** isme paste kar dijiye.

3. Terminal mein ye commands chalaye:

```bash
git add README.md
git commit -m "Added professional README"
git push


