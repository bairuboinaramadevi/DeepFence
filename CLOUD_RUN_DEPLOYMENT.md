
# 🚀🛡️ Deploying DeepFence to Cloud Run from VS Code  
**🔐 Google Cloud Auth + 🔥 Firebase Integration**

---

## ✅ Prerequisites

Before starting, ensure the following are in place:

| Requirement               | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| 🏦 **Google Cloud Account** | Billing enabled and Cloud Run API activated                                  |
| 💻 **VS Code**             | With [Cloud Code Extension](https://cloud.google.com/code/docs/vscode)      |
| 🐳 **Docker Installed**    | For local builds (optional if using Cloud Buildpacks)                        |
| 📦 **Your Project Code**   | Contains a `Dockerfile` or is auto-buildable via Buildpacks                 |
| 🔥 **Firebase Project**    | Initialized with service account key downloaded                            |
| 🔐 **Firebase Admin SDK**  | Installed and integrated into your app code                                 |

---

## 1️⃣ Authenticate VS Code with Google Cloud

1. Open **Visual Studio Code**  
2. Click the **Google Cloud icon** in the sidebar (Cloud Code)  
3. Click ➕ **Sign in to Google Cloud**  
4. Complete browser-based login flow  
5. ✅ Confirm active project at bottom-left status bar

---

## 2️⃣ Prepare Your Application (Cloud Run + Firebase Ready)

### ✔️ Requirements
- Your app **must listen on port `8080`**
- Must have a `Dockerfile` or support **Cloud Buildpacks**

### 🔥 Firebase Integration (Python Example)

#### ➤ Install Firebase Admin SDK
```bash
pip install firebase-admin
```

#### ➤ Initialize Firebase in Code
```python
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Example: Store scan results
db.collection("deepfence-results").add({"result": "secure"})
```

### 🔐 Secure Credentials
- ✅ Copy service account key inside Dockerfile (not recommended)  
- 🌿 Prefer environment variables or Google Secret Manager for production

---

## 3️⃣ Deploy to Cloud Run from VS Code

### 📦 Deployment Steps

1. Open **Cloud Code Sidebar** in VS Code  
2. Right-click your **project folder** or use **Command Palette** (`Ctrl+Shift+P` or `Cmd+Shift+P`)  
3. Search:  
   ```
   Cloud Run: Deploy to Cloud Run
   ```
4. 🧭 Follow the prompts:
   - Select **GCP project**
   - Choose or create a **Cloud Run service**
   - Pick a **region**
   - Choose source: `Dockerfile` or **Cloud Buildpacks**
   - Set **environment variables** like:
     ```bash
     GOOGLE_APPLICATION_CREDENTIALS=/app/keys/firebase-key.json
     ```
   - Choose access level: **Allow unauthenticated?**

✅ VS Code builds → pushes → deploys your app to Cloud Run automatically!

---

## 4️⃣ Monitor Deployment & Access Your App

- 🛠️ Watch the **Output** window for build logs
- 🌐 After deployment, copy or click the **Cloud Run URL**
- 🔍 Paste it in your browser to verify your app is live

---

## 5️⃣ 🔐 Manage Secrets Securely

> Never hardcode Firebase credentials or API keys.

### ✅ Recommended Approaches:
- 🌿 **Environment variables**
- 🔐 **Google Secret Manager**
```bash
gcloud secrets create firebase-key   --data-file="path/to/serviceAccountKey.json"
```

Use Cloud Code or `gcloud` to mount secrets into Cloud Run securely.

---

## 6️⃣ 🔥 Firebase as Backend Database

Your deployed app can now:

- ✅ Store DeepFence scan results to **Firestore** or **Realtime DB**
- 📈 Retrieve logs or summaries
- 🔄 Enable dashboard workflows and visualizations

---

## 🔄 Redeploying & Updating

Make your code changes and repeat:

```bash
Cloud Run: Deploy to Cloud Run
```

🧠 Cloud Code will handle image build and deployment automatically.

---

## 📝 Tips & Debugging

| Tool                   | Use Case                                   |
|------------------------|--------------------------------------------|
| 🔭 **Cloud Run Explorer** | View deployed services, open logs & URLs    |
| 📊 **Firebase Console**   | Monitor data writes, auth rules, analytics |
| 🧾 **Output Logs**        | Watch deployment status and error traces   |

---

## 📚 References

- [🔧 Cloud Code for VS Code](https://cloud.google.com/code/docs/vscode)  
- [🔥 Firebase Admin SDK Setup](https://firebase.google.com/docs/admin/setup)  
- [🛡️ Deepfence Cloud Scanner GitHub](https://github.com/deepfence/)

---

> ✅ This setup lets you **securely deploy DeepFence from VS Code to Google Cloud Run** with **full Firebase integration**, using intelligent workflows and Google-native tools!  
> Stay protected. Stay scalable. ☁️🔥🛡️
