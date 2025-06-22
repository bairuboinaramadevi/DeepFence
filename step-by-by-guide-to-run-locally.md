# DeepFence

This guide provides step-by-step instructions to set up and run your application on your local machine using **VS Code**, **Python**, and **SQLite**.

---

## 🛠 Prerequisites

Make sure the following are installed:

- **Git**: Version control tool  
  👉 [Download Git](https://git-scm.com/downloads)

- **Python & pip**: Programming language and its package installer  
  👉 [Download Python](https://www.python.org/downloads/)

- **VS Code**: Code editor / IDE  
  👉 [Download VS Code](https://code.visualstudio.com/download)

- **SQLite**: No separate installation is usually needed—it’s bundled with Python or your framework (e.g., Django, Flask)

---

## 💡 Recommended VS Code Extensions

For a smoother development experience:

- **Python** (by Microsoft)
- **SQLite** (e.g., "SQLite" by alexcvzz)

---

## 🚀 Setup Steps

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repository-name>.git 
cd <your-repository-name> #cd DeepFence
Replace <your-username> and <your-repository-name> with your actual GitHub details.  ### https://github.com/bairuboinaramadevi/DeepFence.git

2️⃣ Open in VS Code
bash
Copy
Edit
code .
If code . doesn't work, open VS Code manually and go to File > Open Folder...

3️⃣ Install Python Dependencies
It's best to use a virtual environment:

bash
Copy
Edit
# Create a virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows (Command Prompt):
venv\Scripts\activate.bat

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
📝 Tip: If VS Code asks you to select a Python interpreter, choose the one inside your venv.

4️⃣ Environment Variables (If Applicable)
If there's a .env.example file:

bash
Copy
Edit
cp .env.example .env
Edit .env and fill in any required variables like API keys, ports, etc.

5️⃣ Database Setup (SQLite)
No installation is needed for SQLite.

If your app uses database migrations:

For Flask (with Flask-Migrate):
bash
Copy
Edit
flask db init       # only once
flask db migrate
flask db upgrade
These commands will create the SQLite file (e.g., db.sqlite3) and tables.

▶️ Running the Application
Make sure your virtual environment is active before running the app.

From Terminal
bash
Copy
Edit
# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate.bat

# Run the app
python <your_main_app_file>.py


# For Flask:
flask run
From VS Code (Run and Debug)
Open Run and Debug view (Ctrl+Shift+D / Cmd+Shift+D).

Select the right config from dropdown (if launch.json exists).

Press the green ▶️ Start button.

🌐 Accessing the App
Once running, open your browser and go to:

http://localhost:5000 (Flask default)

Check your terminal for the exact URL and port.

