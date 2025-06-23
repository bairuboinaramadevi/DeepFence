	# 🚀🛡️ Running DeepFence on Google Cloud Run

	Google Cloud Run is a managed serverless platform that lets you deploy containerized applications with ease. This guide walks you through deploying DeepFence Cloud Scanner to Cloud Run using the Google Cloud CLI, with rich icons for clarity and visual appeal.

	----------

	## ✅ Prerequisites

	-   🏦  **Google Cloud**  account with billing enabled
	    
	-   🖥️  **Google Cloud SDK (gcloud CLI)**  installed  
	    👉  [Install gcloud](https://cloud.google.com/sdk/docs/install)
	    
	-   🐳  **Docker**  installed (optional, if building images locally)  
	    👉  [Install Docker](https://www.docker.com/get-started)
	    
	-   🔑  **DeepFence Management Console URL & API Key**
	    

	----------

	## 🛠️ Deployment Methods

	You can deploy to Cloud Run in several ways:

	1.  📦  **From a Git Repository**  – Automatically deploy from GitHub or other repos
	    
	2.  🗂️  **Using a Pre-built Container Image**  – Deploy images from Google Container or Artifact Registry
	    
	3.  💻  **Using gcloud CLI**  – Most versatile and controlled approach
	    
	4.  🏗️  **Using Cloud Buildpacks**  – Automatically detect and containerize your app
	    

	----------

	## 📦 Step-by-Step Deployment (Using  `gcloud`  CLI)

	## 1️⃣ Prepare Your Application

	Ensure your app is containerized. If not, create a  `Dockerfile`  in your project root:

	text

	`FROM python:3.9-slim   WORKDIR /app COPY . .   RUN pip install -r requirements.txt EXPOSE 8080   CMD ["python", "app.py"]` 

	🔁  _Adjust the base image, install commands, port, and CMD based on your stack._

	----------

	## 2️⃣ Build and Push the Container Image (Optional)

	If you already have a container image, skip this step. Otherwise:

	bash

	`# 🏗️ Build the image docker build -t gcr.io/<your-project-id>/<your-image-name>:<tag>  .   # 🚀 Push to Google Container Registry docker push gcr.io/<your-project-id>/<your-image-name>:<tag>` 

	_Replace  `<your-project-id>`,  `<your-image-name>`, and  `<tag>`  (e.g., latest)._

	----------

	## 3️⃣ Deploy to Cloud Run

	bash

	`gcloud run deploy <service-name>  \   --image gcr.io/<your-project-id>/<your-image-name>:<tag>  \ --region <your-region>  \ --platform managed \ --allow-unauthenticated` 

	🔧  _Replace placeholders:_

	-   `<service-name>`  – Your Cloud Run service name
	    
	-   `<your-region>`  – e.g., us-central1
	    
	-   Remove  `--allow-unauthenticated`  if you want to require authentication
	    

	----------

	## 4️⃣ 🔗 Retrieve and Test Your Deployment URL

	If the CLI does  **not**  show the service URL after deployment, run:

	bash

	`gcloud run services describe <service-name>  \   --region <your-region>  \ --platform managed \ --format='value(status.url)'` 

	🌐  _Copy and open the URL in your browser to test your deployed app._

	----------

	## ⚙️ Additional Options

	-   📝  **Set Environment Variables:**
	    
	    bash
	    
	    `gcloud run deploy <service-name>  \   --image ... \ --set-env-vars KEY1=value1,KEY2=value2` 
	    
	-   📈  **Scale Configuration:**  
	    Cloud Run auto-scales based on traffic. Configure min/max instances with  `--min-instances`  and  `--max-instances`.
	    
	-   🔄  **Continuous Deployment:**  
	    Enable GitHub-triggered deployments via Cloud Build.
	    
	-   ☁️  **"Run on Google Cloud" Button:**  
	    Add a one-click deployment button to your repo.  
	    👉 See: cloud-run-button GitHub Repo
	    

	----------

	## 🧩 Troubleshooting

	-   🛠️  **Port Mismatch:**  
	    Your app must listen on the same port as declared in  `EXPOSE`  and used by Cloud Run (typically 8080).
	    
	-   🛡️  **Permission Errors:**  
	    Ensure your account has roles like Cloud Run Admin and Service Account User.
	    
	-   🖼️  **Image Build Issues:**  
	    Check for typos or incorrect commands in your Dockerfile.
	    

	----------

	## 📚 Resources

	-   [📖 DeepFence Cloud Scanner Docs](https://community.deepfence.io/threatmapper/docs/cloudscanner/gcp/)
	    
	-   [☁️ Google Cloud Run Documentation](https://cloud.google.com/run/docs/deploying)
	    

	----------

	**Protect your cloud. Deploy DeepFence in minutes!**
