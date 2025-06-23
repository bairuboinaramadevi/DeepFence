# 🛡️ DeepFence

A lightweight Python application powered by **Flask** and **SQLite**, designed for local development using **VS Code**.

----------

## 📋 Table of Contents

-   [🛠 Prerequisites](#-prerequisites)
    
-   [💡 Recommended VS Code Extensions](#-recommended-vs-code-extensions)
    
-   [🚀 Setup Steps](#-setup-steps)
    
    -   [1️⃣ Clone the Repository](#1%EF%B8%8F%E2%83%A3-clone-the-repository)
        
    -   [2️⃣ Open in VS Code](#2%EF%B8%8F%E2%83%A3-open-in-vs-code)
        
    -   [3️⃣ Install Python Dependencies](#3%EF%B8%8F%E2%83%A3-install-python-dependencies)
        
    -   [4️⃣ Environment Variables (Optional)](#4%EF%B8%8F%E2%83%A3-environment-variables-optional)
        
    -   [5️⃣ Database Setup (SQLite)](#5%EF%B8%8F%E2%83%A3-database-setup-sqlite)
        
-   [▶️ Running the Application](#%EF%B8%8F-running-the-application)
    
-   [🌐 Accessing the App](#-accessing-the-app)
    

----------

🛠 Prerequisites
Ensure the following tools are installed on your system before you proceed with setup:

🧰 Tool	🧾 Purpose	🔗 Download Link
Git	Version control system	Download Git
Python + pip	Programming language and package manager	Download Python
VS Code	Code editor / Integrated Development Environment	Download VS Code
SQLite	Lightweight relational database	Bundled with Python or your framework (Flask/Django)

## 💡 Recommended VS Code Extensions

Install these extensions from the VS Code Marketplace:

-   ✅ **Python** (by Microsoft)
    
-   ✅ **SQLite** (e.g., _SQLite_ by _alexcvzz_)
    

----------

## 🚀 Setup Steps

### 1️⃣ Clone the Repository

bash

CopyEdit

`git clone https://github.com/bairuboinaramadevi/DeepFence.git cd DeepFence` 

----------

### 2️⃣ Open in VS Code

bash

CopyEdit

`code .` 

If `code .` doesn't work, manually open VS Code and go to:  
**File > Open Folder > Select `DeepFence`**

----------

### 3️⃣ Install Python Dependencies

We recommend using a **virtual environment**:

bash

CopyEdit

`# Create virtual environment python -m venv venv # Activate it  # macOS / Linux  source venv/bin/activate # Windows - Command Prompt venv\Scripts\activate.bat # Windows - PowerShell .\venv\Scripts\Activate.ps1 # Install dependencies pip install -r requirements.txt` 

> 🧠 _If prompted in VS Code, choose the Python interpreter inside `venv`._

----------

### 4️⃣ Environment Variables (Optional)

If the project contains a `.env.example` file:

bash

CopyEdit

`cp .env.example .env` 

Update `.env` with your configuration values (e.g., API keys, ports, database path).

----------

### 5️⃣ Database Setup (SQLite)

No separate installation needed!

If your app uses **Flask-Migrate**, run:

bash

CopyEdit

`flask db init # (Run only once) flask db migrate
flask db upgrade` 

This will generate the database file (e.g., `db.sqlite3`) and tables.

----------

## ▶️ Running the Application

Ensure your **virtual environment is activated**:

bash

CopyEdit

`# macOS / Linux  source venv/bin/activate # Windows venv\Scripts\activate.bat` 

Then run:

bash

CopyEdit

`python <your_main_app_file>.py # OR for Flask apps: flask run` 

----------

## 🌐 Accessing the App

Once running, navigate to:

arduino

CopyEdit

`http://localhost:5000` 

> ℹ️ Check your terminal for the exact URL and port.

----------

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

----------

## 📄 License

This project is licensed under the MIT License. See LICENSE for details.
