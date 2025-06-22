# Running Your Application on Google Cloud Run

Google Cloud Run is a managed serverless platform that lets you deploy containerized applications. This guide provides instructions on how to deploy your application to Cloud Run.

## Prerequisites

* A Google Cloud account with billing enabled.
* The Google Cloud SDK (gcloud CLI) installed.
* (Optional) Docker installed, if you need to build your own container image.

## Methods for Deployment

You can deploy to Cloud Run using several methods:

1.  **From a Git Repository:** Cloud Run can directly deploy from your source code in a Git repository (e.g., GitHub). This is often the simplest method.
2.  **Using a Pre-built Container Image:** If you have already built a Docker image for your application, you can deploy it from Google Container Registry or Artifact Registry.
3.  **Using the gcloud CLI:** The `gcloud` command-line tool provides fine-grained control over deployment.
4.  **Using Cloud Buildpacks:** Cloud Run can automatically detect the language of your application and build a container image using Google Cloud Buildpacks.

## Detailed Steps

Here's a breakdown of the typical steps, focusing on using the gcloud CLI (the most versatile method):

### 1. Prepare your application

* Ensure your application is containerized. If it's not already in a Docker container, you'll need to create a `Dockerfile` in the root of your project. Here's a basic example:

    ```dockerfile
    FROM <base_image>  # e.g., python:3.9-slim, node:16
    WORKDIR /app
    COPY . .
    RUN <install_dependencies> # e.g., pip install -r requirements.txt, npm install
    CMD <start_command>      # e.g., python app.py, npm start
    EXPOSE <port>           # e.g., 8080 (very important)
    ```

    * Replace `<base_image>`, `<install_dependencies>`, `<start_command>`, and `<port>` with the appropriate values for your application.  **Make sure the port your application listens on matches the `EXPOSE`d port.**

### 2. Build and push your container image (if necessary)

* If you're using a pre-built image, skip this step.
* If you have a `Dockerfile`, build the image:

    ```bash
    docker build -t gcr.io/<your-project-id>/<your-image-name>:<tag> .
    ```

    * Replace `<your-project-id>`, `<your-image-name>`, and `<tag>` with your Google Cloud project ID, a name for your image, and a tag (e.g., `latest`).
* Push the image to Google Container Registry or Artifact Registry:

    ```bash
    docker push gcr.io/<your-project-id>/<your-image-name>:<tag>
    ```

### 3. Deploy to Cloud Run

* Use the `gcloud run deploy` command:

    ```bash
    gcloud run deploy <service-name> \
        --image gcr.io/<your-project-id>/<your-image-name>:<tag> \
        --region <your-region> \
        --platform managed \
        --allow-unauthenticated # If you want your service publicly accessible
    ```

    * Replace `<service-name>` with a name for your Cloud Run service.
    * Replace `<your-region>` with a Google Cloud region (e.g., `us-central1`).
    * If you require authentication, remove the `--allow-unauthenticated` flag.

### 4. Test your deployment

* After deployment, Cloud Run will provide a URL. Visit this URL in your browser to test your application.

##  Additional Options and Considerations

* **Environment Variables:** Use the `--set-env-vars` flag to pass environment variables to your application:

    ```bash
    gcloud run deploy <service-name> --image ... --set-env-vars KEY1=value1,KEY2=value2
    ```

* **Scaling:** Cloud Run automatically scales your application based on traffic. You can configure minimum and maximum instances.
* **Continuous Deployment:** Set up continuous deployment from your Git repository so that changes to your code automatically trigger a new deployment.
* **Cloud Run Button:** For public repositories, you can add a "Run on Google Cloud" button to your `README.md`, allowing users to deploy your application with a single click.  See the [GoogleCloudPlatform/cloud-run-button](https://github.com/GoogleCloudPlatform/cloud-run-button) repository for details.

## Troubleshooting

* **Port Mismatch:** Ensure the port your application listens on inside the container matches the `EXPOSE` directive in your `Dockerfile` and any port settings in Cloud Run.
* **Permissions:** Make sure your Google Cloud account has the necessary permissions (e.g., Cloud Run Admin, Service Account User).
* **Image Errors:** If you're using a custom container, double-check your `Dockerfile` for errors.
