:

🛡️ DeepFence
A lightweight Python application powered by Flask and SQLite, designed for seamless local development using VS Code.

📋 Table of Contents
🛠 Prerequisites

💡 Recommended VS Code Extensions

🚀 Setup Steps

1️⃣ Clone the Repository

2️⃣ Open in VS Code

3️⃣ Install Python Dependencies

4️⃣ Environment Variables (Optional)

5️⃣ Database Setup (SQLite)

▶️ Running the Application

🌐 Accessing the App

🤝 Contributing

📄 License

🛠 Prerequisites
Ensure the following tools are installed on your system:

🔧 Git — Version control
👉 Download Git

🐍 Python + pip — Programming language and package manager
👉 Download Python

🖥️ VS Code — Code editor / IDE
👉 Download VS Code

🗄️ SQLite — Lightweight database
Typically bundled with Python or web frameworks like Flask/Django

💡 Recommended VS Code Extensions
Enhance your development experience by installing:

✅ Python (by Microsoft)

✅ SQLite (e.g., SQLite by alexcvzz)

🚀 Setup Steps
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/bairuboinaramadevi/DeepFence.git
cd DeepFence
2️⃣ Open in VS Code
bash
Copy
Edit
code .
If code . doesn't work, open VS Code manually and go to:
File > Open Folder > Select DeepFence

3️⃣ Install Python Dependencies
We recommend setting up a virtual environment:

bash
Copy
Edit
# Create virtual environment
python -m venv venv

# Activate it

# macOS / Linux
source venv/bin/activate

# Windows - Command Prompt
venv\Scripts\activate.bat

# Windows - PowerShell
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
🧠 Choose the Python interpreter inside venv if prompted in VS Code.

4️⃣ Environment Variables (Optional)
If the project includes a .env.example file:

bash
Copy
Edit
cp .env.example .env
Edit .env to fill in any required variables like:

API keys

Port numbers

Database paths

5️⃣ Database Setup (SQLite)
No installation needed for SQLite.

If your app uses Flask-Migrate, initialize the database:

bash
Copy
Edit
# Only once
flask db init

# Create migration scripts
flask db migrate

# Apply migrations
flask db upgrade
This will create the database file (e.g., db.sqlite3) and required tables.

▶️ Running the Application
Ensure your virtual environment is activated:

bash
Copy
Edit
# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate.bat
Then run the app:

bash
Copy
Edit
# General
python <your_main_app_file>.py

# For Flask apps
flask run
🌐 Accessing the App
Once running, open your browser and go to:

bash
Copy
Edit
http://localhost:5000
ℹ️ The exact URL and port will be shown in your terminal.

