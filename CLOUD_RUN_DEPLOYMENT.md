🚀🛡️ Running DeepFence on Google Cloud Run
Google Cloud Run is a fully managed serverless platform that allows you to deploy containerized applications easily. Here's a visually enhanced guide to help you deploy DeepFence Cloud Scanner on Cloud Run using the gcloud CLI.

✅ Prerequisites
🏦 Google Cloud Account

Billing must be enabled

👉 Create GCP Account

💻 Google Cloud SDK (gcloud CLI)

Required for deploying via CLI

👉 Install gcloud

🐳 Docker (Optional if not using pre-built image)

👉 Install Docker

🔑 DeepFence API Key & Console URL

Required for configuring scan credentials

🛠️ Deployment Methods
Choose a method that suits your workflow:

📁 From Git Repository – Auto-deploy via GitHub/GitLab

🧊 Pre-built Container Image – Use images from Artifact Registry

🖥️ gcloud CLI – 🔥 Most flexible & controlled

🧱 Cloud Buildpacks – Auto-detects and containerizes apps

📦 Step-by-Step Deployment (via gcloud CLI)
1️⃣ Prepare Your Application
Ensure your app is containerized with a Dockerfile:

dockerfile
Copy
Edit
# 📌 Base Image
FROM python:3.9-slim

# 📁 Set working directory
WORKDIR /app

# 📂 Copy code
COPY . .

# 📦 Install dependencies
RUN pip install -r requirements.txt

# 🌐 Expose the port used by Cloud Run
EXPOSE 8080

# 🚀 Run the app
CMD ["python", "app.py"]
⚙️ Modify as per your stack (Node.js, Go, Java, etc.)

2️⃣ Build & Push the Container Image
bash
Copy
Edit
# 🏗️ Build image locally
docker build -t gcr.io/<your-project-id>/<your-image-name>:<tag> .

# 🚀 Push to Google Container Registry
docker push gcr.io/<your-project-id>/<your-image-name>:<tag>
📝 Replace:

<your-project-id> → your GCP project ID

<your-image-name> → e.g., deepfence-scanner

<tag> → e.g., latest

3️⃣ Deploy to Cloud Run
bash
Copy
Edit
gcloud run deploy <service-name> \
  --image gcr.io/<your-project-id>/<your-image-name>:<tag> \
  --region <your-region> \
  --platform managed \
  --allow-unauthenticated
🔧 Replace:

<service-name> → e.g., deepfence-cloud-run

<your-region> → e.g., us-central1

Remove --allow-unauthenticated if you want secured access

4️⃣ 🔍 Retrieve & Test the URL
If the CLI doesn't display the URL after deployment:

bash
Copy
Edit
gcloud run services describe <service-name> \
  --region <your-region> \
  --platform managed \
  --format='value(status.url)'
🌐 Paste the URL in your browser to verify the app is running.

⚙️ Advanced Options
📝 Environment Variables

bash
Copy
Edit
gcloud run deploy <service-name> \
  --image ... \
  --set-env-vars KEY1=value1,KEY2=value2
📊 Scaling Config

bash
Copy
Edit
--min-instances=1 \
--max-instances=10
🔁 Enable Continuous Deployment

Set up GitHub Actions or Cloud Build triggers.

☁️ Add "Run on Google Cloud" Button
👉 cloud-run-button GitHub

🧩 Troubleshooting
Issue	Cause	Solution
⚠️ Port Binding	App not listening on correct port	Ensure EXPOSE 8080 and app uses port 8080
🔐 Permission Denied	Missing roles	Assign Cloud Run Admin and Service Account User
🐳 Docker Build Fails	Syntax errors	Review your Dockerfile for issues

📚 Helpful Resources
📖 DeepFence Cloud Scanner Docs

☁️ Google Cloud Run Documentation

🛡️ Secure your Cloud in Minutes – Deploy DeepFence Today!
