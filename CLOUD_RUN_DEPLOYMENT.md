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
