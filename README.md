🩺 ENT Specialist Chatbot

AI-powered healthcare chatbot that answers Ear, Nose, and Throat (ENT) related queries using Google Gemini 2.5 Flash and Streamlit UI.
Developed as part of the Innomatics Research Labs Internship Project.

🚀 Features

ENT specialist conversational assistant

Short and precise medical guidance (2–3 lines response)

Gemini-powered contextual chat

Session-based chat memory

Streamlit interactive UI

AWS EC2 deployment ready

👨‍💻 Team Members

Saravanan – Frontend & Chatbot Development

Vasanth – AWS EC2 Deployment

Sindhu – Gemini API Integration

🛠 Tech Stack

Python

Streamlit

Google Gemini API

AWS EC2

dotenv

📂 Project Structure
ent-specialist-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env

⚙️ Setup & Run Locally
1️⃣ Clone repo
git clone https://github.com/your-username/ent-specialist-chatbot.git
cd ent-specialist-chatbot

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add Gemini API key

Create .env file:

GEMINI_API_KEY=your_api_key_here

5️⃣ Run app
streamlit run app.py

☁️ Deployment

The application is deployed using AWS EC2 with Streamlit server configuration.

Basic deployment flow:

Launch EC2 instance

Install Python & dependencies

Clone repository

Run Streamlit app

Configure security group (port 8501)

📸 Demo



⚠️ Disclaimer

This chatbot provides general ENT guidance only and should not replace professional medical consultation.

⭐ Future Improvements

Voice input support

Medical history memory

Multi-specialist expansion

Authentication system

RAG-based medical knowledge integration

🙌 Acknowledgment

Thanks to Innomatics Research Labs for providing the internship opportunity and project guidance.
