Graph LLM System (AI-Powered Data Explorer)
🧠 Overview

This project is a full-stack AI system that allows users to query structured data using natural language. It converts user queries into SQL using an LLM, executes them on a database, and visualizes relationships using an interactive graph.

✨ Key Features
🔍 Natural Language → SQL conversion using LLM
📊 Graph-based visualization of data relationships
💬 Interactive chat interface (like ChatGPT)
⚡ Real-time query execution
🛡️ Guardrails to prevent invalid or unsafe queries
🎯 Clean UI with chat history and loading states
🏗️ Architecture
User → React Chat UI
     → Django REST API
     → LLM (Groq)
     → SQL → Database
     → Response → Graph Visualization
🗄️ Tech Stack
Frontend
React (Vite)
react-force-graph-2d
Backend
Django
Django REST Framework
NetworkX
AI / LLM
Groq API (llama-3.1-8b-instant)
Database
SQLite (default Django DB)
🔗 Graph Design
Nodes
Customer
Order
Edges
Customer → Order (PLACED)

Graph is built using NetworkX and rendered using react-force-graph.

🤖 LLM Prompting Strategy

The LLM is guided using strict schema grounding:

core_customer(id, name)
core_order(id, customer_id)
Rules enforced:
Only use provided tables
No hallucinated columns
Return only SQL (no explanations)
Example Prompt
Q: show all orders  
A: SELECT * FROM core_order;

Q: list all customers  
A: SELECT * FROM core_customer;
🛡️ Guardrails & Safety
Restricted queries to dataset-related context
Replaced incorrect table names:
orders → core_order
customers → core_customer
Added backend exception handling
Prevented invalid SQL execution
⚠️ Challenges & Solutions
1. LLM Hallucination
Solved via schema grounding and strict prompts
2. API Failures
Added try/catch and safe JSON parsing
3. Model Deprecation
Updated Groq model dynamically
4. Frontend-Backend Sync
Fixed CORS and API URL issues
🎯 Features Demonstrated
Full-stack system design
LLM integration into backend workflows
Graph-based data modeling
Prompt engineering & guardrails
Debugging and error handling
▶️ How to Run Locally
🔹 Backend
cd backend
pip install -r requirements.txt
python manage.py runserver
🔹 Frontend
cd frontend
npm install
npm run dev
🌐 Deployment
Frontend: Vercel
Backend: Render

👉 Live Demo: https://your-app.vercel.app
👉 Backend API: https://your-backend.onrender.com

📂 Project Structure
graph-llm-system/
├── backend/
├── frontend/
├── sessions/
└── README.md
📄 AI Coding Workflow

AI tools were used for:

System design and architecture planning
Generating backend APIs and frontend components
Prompt engineering for LLM
Debugging errors and refining logic
🚀 Future Improvements
Multi-table relationships (invoices, payments)
Graph node highlighting based on queries
Conversational memory
Advanced analytics queries
Authentication system


💡 Final Note

This project demonstrates the integration of LLMs with traditional backend systems to create intelligent, user-friendly data exploration tools.

It reflects real-world challenges like prompt design, API instability, and system integration — and how to solve them effectively.