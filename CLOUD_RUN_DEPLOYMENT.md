# 🚀🛡️ Deploying DeepFence to Cloud Run from VS Code  
**🔐 Google Cloud Authentication + 🔥 Firebase Database Integration**

---

## ✅ Prerequisites

Before you begin, ensure the following:

- 🏦 **Google Cloud account** with billing enabled  
- ☁️ **Cloud Run API** enabled on your project  
- 🧑‍💻 **VS Code** installed  
- 🧩 **Cloud Code extension** for VS Code  
- 🐳 **Docker installed** (for local builds)  
- 📁 Your project code with:
  - 🐋 `Dockerfile` *or*
  - ⚙️ Compatible entry point (for **Cloud Buildpacks**)  
- 🔥 **Firebase project** set up with:
  - 🔐 **Firebase Admin SDK** integrated in your app  
  - 🗂️ **Service account key JSON**

---

## 1️⃣ Authenticate VS Code with Google Cloud

🔓 Secure your environment with Google Cloud:

1. Open **VS Code**  
2. Click on **Cloud Code sidebar** (🟦 Google Cloud icon)  
3. Select **Sign in to Google Cloud**  
4. Complete the authentication flow  
5. Confirm correct project in the **Cloud Code status bar**

---

## 2️⃣ Prepare Your Application (with Firebase Integration)

📦 Make your app Cloud Run–ready:

- Ensure it:
  - Listens on **port `8080`**  
  - Contains a **Dockerfile** or uses **Cloud Buildpacks**  

### 🔥 Firebase Integration (Python Example)

Install Firebase Admin SDK:

```bash
pip install firebase-admin
Initialize Firebase in your app:

python
Copy
Edit
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('path/to/serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Example usage
db.collection('deepfence-results').add({'result': 'secure'})
⚠️ Make sure your Dockerfile:

Copies the service account key, or

Uses env vars or Secret Manager for secure credentials injection

3️⃣ Deploy to Cloud Run from VS Code
🚀 Deploy your app in a few clicks:

Open the Cloud Code sidebar

Right-click the project folder or open Command Palette (Ctrl+Shift+P / Cmd+Shift+P)

Select ➡️ Cloud Run: Deploy to Cloud Run

🧭 Follow the prompts:
Select your GCP project

Choose or create a Cloud Run service

Pick your region

Choose image source: Dockerfile or Buildpacks

Set environment variables, e.g.:

GOOGLE_APPLICATION_CREDENTIALS for Firebase

Choose access: Authenticated or Unauthenticated

✅ Cloud Code will build → push → deploy automatically

4️⃣ Monitor Deployment & Access Service
📺 Watch deployment status in the Output window

🌐 Copy or click the service URL

✅ Verify it’s running live on Cloud Run

5️⃣ 🔐 Manage Secrets Securely
🛡️ Use one of the following:

🔑 Secret Manager

🌿 Environment variables

❌ Never hardcode secrets like API keys or service account JSONs in source code

6️⃣ 🔥 Using Firebase as Your Database
📡 Your Cloud Run app can now:

Read/write DeepFence scan results, logs, or metadata

Store and retrieve data via Firestore or Realtime DB

Use it for reporting, dashboards, or alerts

🔄 Redeploying & Updating
♻️ Make code changes → redeploy:

bash
Copy
Edit
Cloud Run: Deploy to Cloud Run
✅ It will rebuild and redeploy your latest updates.

📝 Tips
📊 Use Cloud Run Explorer in VS Code:

View logs

Manage services

Open deployed URLs

🔥 Use Firebase Console to:

View real-time data

Monitor usage & security rules

🧾 Debugging:

Use the Output window and Cloud Run logs

📚 References
🧩 Cloud Code for VS Code

🔥 Firebase Admin SDK Setup

🔍 Deepfence Cloud Scanner GitHub

🚀 This guide enables end-to-end deployment from VS Code → Cloud Run, with secure auth and Firebase-backed database 🔥🛡️💻.
