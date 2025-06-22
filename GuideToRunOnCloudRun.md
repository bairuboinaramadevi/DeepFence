# 🚀 Running DeepFence on Google Cloud Run

Google Cloud Run is a managed serverless platform that lets you deploy containerized applications. This guide walks you through deploying your app to Cloud Run.

---

## ✅ Prerequisites

- A **Google Cloud** account with billing enabled  
- **Google Cloud SDK (gcloud CLI)** installed  
  👉 [Install gcloud](https://cloud.google.com/sdk/docs/install)  
- (Optional) **Docker** installed if you’re building container images locally  
  👉 [Install Docker](https://www.docker.com/get-started)

---

## 🛠️ Deployment Methods

You can deploy to Cloud Run in several ways:

1. **From a Git Repository** – Automatically deploy from GitHub or other repos  
2. **Using a Pre-built Container Image** – Deploy images from Google Container or Artifact Registry  
3. **Using gcloud CLI** – Most versatile and controlled approach  
4. **Using Cloud Buildpacks** – Automatically detect and containerize your app

---

## 📦 Step-by-Step Deployment (Using `gcloud` CLI)

### 1️⃣ Prepare Your Application

Make sure your app is containerized. If not, create a `Dockerfile` in your project root:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
EXPOSE 8080

CMD ["python", "app.py"]
🔁 Adjust the base image, install, port, and CMD based on your stack.

2️⃣ Build and Push the Container Image (Optional)
If you already have an image, skip this step. Otherwise, build and push:

bash
Copy
Edit
# Build the image
docker build -t gcr.io/<your-project-id>/<your-image-name>:<tag> .

# Push to Google Container Registry
docker push gcr.io/<your-project-id>/<your-image-name>:<tag>
Replace <your-project-id>, <your-image-name>, and <tag> (e.g., latest).

3️⃣ Deploy to Cloud Run
Run the following command:

bash
Copy
Edit
gcloud run deploy <service-name> \
  --image gcr.io/<your-project-id>/<your-image-name>:<tag> \
  --region <your-region> \
  --platform managed \
  --allow-unauthenticated
🔧 Replace placeholders:

<service-name> – Your Cloud Run service name

<your-region> – e.g., us-central1

Remove --allow-unauthenticated if you want to require auth

4️⃣ Test Your Deployment
After deployment, the CLI will return a live URL.
Visit this URL in your browser to test your deployed app.

⚙️ Additional Options
Set Environment Variables:

bash
Copy
Edit
gcloud run deploy <service-name> \
  --image ... \
  --set-env-vars KEY1=value1,KEY2=value2
Scale Configuration:
Cloud Run auto-scales based on traffic. You can configure min/max instances using flags like --min-instances and --max-instances.

Continuous Deployment:
Enable GitHub-triggered deployments via Cloud Build.

"Run on Google Cloud" Button:
Add a one-click deployment button to your repo.
👉 See: cloud-run-button GitHub Repo

🧩 Troubleshooting
Port Mismatch:
Your app must listen on the same port as the one declared in EXPOSE and used by Cloud Run (typically 8080).

Permission Errors:
Ensure your account has roles like Cloud Run Admin and Service Account User.

Image Build Issues:
Check for typos or incorrect commands in your Dockerfile.

