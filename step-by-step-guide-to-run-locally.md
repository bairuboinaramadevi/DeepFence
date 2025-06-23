# DeepFence - Lightweight Flask & SQLite App

DeepFence is a lightweight Python application designed for rapid local development and prototyping. Built with  **Flask**  and  **SQLite**, it offers a seamless workflow for developers using  **VS Code**. The app demonstrates best practices for structuring Flask projects, managing SQLite databases, and building simple web interfaces.

----------

## 📋 Table of Contents

-   [🛠 Prerequisites](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#-prerequisites)
    
-   [💡 Recommended VS Code Extensions](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#-recommended-vs-code-extensions)
    
-   [🚀 Setup Steps](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#-setup-steps)
    
    -   [1️⃣ Clone the Repository](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#1%EF%B8%8F%E2%83%A3-clone-the-repository)
        
    -   [2️⃣ Open in VS Code](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#2%EF%B8%8F%E2%83%A3-open-in-vs-code)
        
    -   [3️⃣ Install Python Dependencies](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#3%EF%B8%8F%E2%83%A3-install-python-dependencies)
        
    -   [4️⃣ Environment Variables (Optional)](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#4%EF%B8%8F%E2%83%A3-environment-variables-optional)
        
    -   [5️⃣ Database Setup (SQLite)](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#5%EF%B8%8F%E2%83%A3-database-setup-sqlite)
        
-   [▶️ Running the Application](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#%EF%B8%8F-running-the-application)
    
-   [🌐 Accessing the App](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#-accessing-the-app)
    
-   [🤝 Contributing](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#-contributing)
    
-   [📄 License](https://www.perplexity.ai/search/deepfence-a-lightweight-python-m.5tiYo9QPS.wBo_9Ma9_w#-license)
    

----------

## 🛠 Prerequisites

-   **Git**  — Version control
    
-   **Python 3.8+**  — Programming language
    
-   **pip**  — Python package manager
    
-   **VS Code**  — Code editor / IDE
    
-   **SQLite**  — Lightweight database (bundled with Python)
    

----------

## 💡 Recommended VS Code Extensions

-   **Python**  (by Microsoft)
    
-   **SQLite**  (e.g.,  _SQLite_  by  _alexcvzz_)
    

----------

## 🚀 Setup Steps

## 1️⃣ Clone the Repository

bash

`git clone https://github.com/bairuboinaramadevi/DeepFence.git` 
`cd DeepFence` 

## 2️⃣ Open in VS Code

 open VS Code manually and go to:  
**File > Open Folder > Select  `DeepFence`**

----------

## 3️⃣ Install Python Dependencies

## 🔄 Create & Activate Virtual Environment

bash

`python -m venv venv` 

**Activate the environment:**

-   **macOS / Linux:**
    
    bash
    
    `source venv/bin/activate` 
    
-   **Windows – Command Prompt:**
    
    text
    
    `venv\Scripts\activate.bat` 
    
-   **Windows – PowerShell:**
    
    powershell
    
    `.\venv\Scripts\Activate.ps1` 
    

----------

## 📦 Install Dependencies

bash

`pip install -r requirements.txt` 

> _If VS Code prompts you to select an interpreter, choose the one from  `./venv`._

----------

## 4️⃣ Environment Variables (Optional)

If a  `.env.example`  file is present:

bash

`cp .env.example .env` 

Edit  `.env`  and configure required variables (e.g., Flask secret key, DB path).

----------

## 5️⃣ Database Setup (SQLite)

If using Flask-Migrate for migrations:

bash

`flask db init flask db migrate flask db upgrade` 

These commands will generate the SQLite database file (e.g.,  `db.sqlite3`).  
Alternatively, you can initialize the database using a schema file and Python code[1](https://flask.palletsprojects.com/en/stable/patterns/sqlite3/)[2](https://stackoverflow.com/questions/74590346/search-function-in-flask-with-sqlite)[3](https://www.scribd.com/document/852424953/Flask-SQLite-HTML-Form-Notes).

----------

## ▶️ Running the Application

Activate your virtual environment:

bash

`# macOS / Linux source venv/bin/activate # Windows venv\Scripts\activate.bat` 

Then start the app:

bash

`# For Flask apps flask run # Or, if you have a main script python app.py` 

----------

## 🌐 Accessing the App

Visit in your browser:

text

`http://localhost:5000` 

> Check your terminal for the actual port if it's customized.

----------

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

----------

## 📄 License

This project is licensed under the MIT License.

----------

