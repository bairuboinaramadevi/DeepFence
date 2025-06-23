# 🚀🛡️ Running DeepFence on Google Cloud Run

Google Cloud Run is a fully managed serverless platform that allows you to deploy containerized applications easily. Here’s a visually enhanced, step-by-step guide to deploying DeepFence Cloud Scanner on Cloud Run using the gcloud CLI.

----------

## ✅ Prerequisites

-   🏦  **Google Cloud Account**  
    Billing must be enabled  
    👉  [Create GCP Account](https://cloud.google.com/)
    
-   💻  **Google Cloud SDK (gcloud CLI)**  
    Required for deploying via CLI  
    👉  [Install gcloud](https://cloud.google.com/sdk/docs/install)
    
-   🐳  **Docker**  (Optional if not using pre-built image)  
    👉  [Install Docker](https://www.docker.com/get-started)
    
-   🔑  **DeepFence API Key & Console URL**  
    Required for configuring scan credentials
    

----------

## 🛠️ Deployment Methods

Choose a method that suits your workflow:

-   📁  **From Git Repository**  – Auto-deploy via GitHub/GitLab
    
-   🧊  **Pre-built Container Image**  – Use images from Artifact Registry
    
-   🖥️  **gcloud CLI**  – 🔥 Most flexible & controlled
    
-   🧱  **Cloud Buildpacks**  – Auto-detects and containerizes apps
    

----------

## 📦 Step-by-Step Deployment (via gcloud CLI)

## 1️⃣ Prepare Your Application

Ensure your app is containerized with a  `Dockerfile`:

text

`# 📌 Base Image FROM python:3.9-slim   # 📁 Set working directory WORKDIR /app   # 📂 Copy code COPY . .   # 📦 Install dependencies RUN pip install -r requirements.txt   # 🌐 Expose the port used by Cloud Run EXPOSE 8080   # 🚀 Run the app CMD ["python", "app.py"]` 

> ⚙️  _Modify as per your stack (Node.js, Go, Java, etc.)_

----------

## 2️⃣ Build & Push the Container Image

bash

`# 🏗️ Build image locally docker build -t gcr.io/<your-project-id>/<your-image-name>:<tag>  .   
#### 🚀 Push to Google Container Registry docker push gcr.io/<your-project-id>/<your-image-name>:<tag>` 

-   📝 Replace:
    
    -   `<your-project-id>`  → your GCP project ID
        
    -   `<your-image-name>`  → e.g., deepfence-scanner
        
    -   `<tag>`  → e.g., latest
        

----------

## 3️⃣ Deploy to Cloud Run

bash

`gcloud run deploy <service-name>  \   --image gcr.io/<your-project-id>/<your-image-name>:<tag>  \ --region <your-region>  \ --platform managed \ --allow-unauthenticated` 

-   🔧 Replace:
    
    -   `<service-name>`  → e.g., deepfence-cloud-run
        
    -   `<your-region>`  → e.g., us-central1
        
    -   Remove  `--allow-unauthenticated`  if you want secured access
        

----------

## 4️⃣ 🔍 Retrieve & Test the URL

If the CLI doesn't display the URL after deployment, run:

bash

`gcloud run services describe <service-name>  \   --region <your-region>  \ --platform managed \ --format='value(status.url)'` 

-   🌐  _Paste the URL in your browser to verify the app is running._
    

----------

## ⚙️ Advanced Options

-   📝  **Environment Variables**
    
    bash
    
    `gcloud run deploy <service-name>  \   --image ... \ --set-env-vars KEY1=value1,KEY2=value2` 
    
-   📊  **Scaling Config**
    
    bash
    
    `--min-instances=1  \ --max-instances=10` 
    
-   🔁  **Enable Continuous Deployment**  
    Set up GitHub Actions or Cloud Build triggers.
    
-   ☁️  **Add "Run on Google Cloud" Button**  
    👉  [cloud-run-button GitHub](https://github.com/GoogleCloudPlatform/cloud-run-button)
    

----------

## 🧩 Troubleshooting

⚠️ Port Binding

Ensure  `EXPOSE 8080`  and app uses port 8080

🔐 Permission Denied

Assign Cloud Run Admin & Service Account User roles

🐳 Docker Build Fails

Review your Dockerfile for issues

----------

🛡️  **Secure your Cloud in Minutes – Deploy DeepFence Today!**
