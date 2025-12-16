AI-Based Chatbot Application
📌 Project Overview

This project is an AI-based chatbot developed for company use to handle common queries related to products and services. The chatbot uses Natural Language Processing (NLP) to understand user intent and respond with relevant, human-like answers.

Currently, the system uses a simple HTML frontend and a Flask-based Python backend, making it lightweight, modular, and easy to extend in the future. 

🧠 Key Features

AI-powered chatbot with intent-based responses

Randomized responses for more natural conversations

NLP processing using spaCy

Flask backend with REST API support

JSON-based intent handling

Easy integration with any frontend

Designed for scalability and future ML model upgrades

🛠️ Technology Stack
Frontend

HTML (basic UI for now)

Backend

Python

Flask (API & routing)

spaCy (NLP processing)

Machine Learning / NLP

Intent-based NLP

Google Colab used for experimentation and model testing 

📂 Project Structure
AI-Chatbot/
│
├── app.py                # Main Flask application
├── chatbot.py            # Chatbot logic & response handling
├── intents.json          # Intents, sample questions & responses
├── templates/
│   └── index.html        # Frontend HTML file
├── static/
│   └── style.css         # (Optional) Styling
└── README.md             # Project documentation 

⚙️ How It Works

User enters a message in the HTML frontend

Message is sent to Flask backend via a POST request

Backend processes the input using NLP (spaCy)

Intent is identified from intents.json

A random response is selected from the matched intent

Response is returned as JSON and displayed on the UI

🧪 Sample Testing
Example Questions:

Q: Tell me about WebXpress
A: Provides company overview or product-related information

Q: What are the features of your products?
A: Displays features and overview of the TMS (Transportation Management System)

Supported topics include:

Product overview

TMS details

Features

Company information 

![alt text](<Screenshot 2025-12-16 160345.png>)

![alt text](<Screenshot 2025-12-16 160828.png>) 

🚀 Running the Project
1. Install Dependencies
pip install flask spacy
python -m spacy download en_core_web_sm

2. Start the Application
python app.py

3. Access the Chatbot

Open your browser and go to:

http://127.0.0.1:5000/

🔮 Future Enhancements

Advanced ML model training

Database integration

User authentication

Admin panel for managing intents

Multi-language support

Improved frontend (React / Vue)

🏢 Use Case

This chatbot was created as a company project to:

Automate responses to common customer queries

Improve customer engagement

Reduce manual support effort

🤝 Conclusion

This project demonstrates a solid foundation for an AI chatbot using Flask and NLP. It is modular, easy to understand, and well-suited for further enhancements based on business needs.