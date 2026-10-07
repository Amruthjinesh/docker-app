# Docker App – Jenkins CI/CD with Automatic Rollback

A DevOps learning project demonstrating how **GitHub, Jenkins, Docker, Python, and ngrok** work together to automatically test, build, deploy, and monitor a containerized web application.

## 📌 Project Overview

This project contains a simple Python web application running inside a Docker container.

The application runs on port `8000`.

### Current Deployment Flow

```text
Developer
   ↓
GitHub
   ↓
GitHub Webhook
   ↓
Jenkins
   ↓
Python Test
   ↓
Docker Image Build
   ↓
Docker Container
   ↓
Health Check
   ↓
Application
```

If the deployment fails:

```text
Health Check ❌
      ↓
Jenkins detects failure
      ↓
Automatic Rollback
      ↓
Previous Docker Image
      ↓
Application Restored ✅
```

## 🛠️ Technologies Used

* Git
* GitHub
* GitHub Webhooks
* Jenkins
* Docker
* Docker Desktop
* Python
* Windows
* AWS EC2
* ngrok

> **Note:** AWS EC2 was used during earlier practice. The current Jenkins and Docker setup runs locally on Windows using Jenkins installed through the MSI installer and Docker Desktop.

## 📁 Project Structure

```text
docker-app/
│
├── app.py
├── Dockerfile
├── Jenkinsfile
└── README.md
```

## 🐍 Application

The application is written in Python and uses the built-in Python HTTP server.

It listens on:

```text
0.0.0.0:8000
```

The application displays:

```text
DevOps Dashboard - Version 40
```

### Test Locally

```powershell
curl http://localhost:8000
```

A successful response returns:

```text
HTTP 200 OK
```

## 🐳 Docker

The application is packaged into a Docker image using the `Dockerfile`.

### Build Manually

```powershell
docker build -t devops-app .
```

### Run Manually

```powershell
docker run -d --name devops-app -p 8000:8000 devops-app
```

### Check Container

```powershell
docker ps
```

### Test Application

```powershell
curl http://localhost:8000
```

## 🔧 Jenkins CI/CD

Jenkins is installed locally on Windows using the **Jenkins MSI installer**.

Jenkins automatically starts the pipeline when a change is pushed to the GitHub repository.

### Jenkins Pipeline Stages

```text
1. Checkout Repository
        ↓
2. Test Python Application
        ↓
3. Build Docker Image
        ↓
4. Save Previous Image
        ↓
5. Stop Old Container
        ↓
6. Run New Container
        ↓
7. Health Check
```

### Python Test

Jenkins checks the Python application for syntax errors:

```text
python -m py_compile app.py
```

### Docker Image Versioning

Each Jenkins build creates a versioned Docker image using the Jenkins build number.

Example:

```text
devops-app:build-46
devops-app:build-48
```

This makes it possible to identify and restore previous application versions.

## 🔄 Automatic Rollback

The pipeline includes an automatic rollback mechanism.

Before deploying a new version, Jenkins identifies the Docker image currently being used by the running container.

Example:

```text
Previous image: devops-app:build-46
```

Jenkins then deploys the new image.

If the health check succeeds:

```text
New Deployment
      ↓
Health Check ✅
      ↓
Pipeline SUCCESS
```

If the health check fails:

```text
New Deployment
      ↓
Health Check ❌
      ↓
Jenkins Failure Handler
      ↓
Stop Failed Container
      ↓
Run Previous Image
      ↓
Rollback Complete ✅
```

### Rollback Test

The rollback mechanism was tested by intentionally changing the health check from:

```text
http://localhost:8000
```

to:

```text
http://localhost:9999
```

The deployment failed as expected.

Jenkins detected the failure and automatically rolled back to:

```text
devops-app:build-46
```

The application was then verified with:

```text
HTTP 200 OK
```

After testing, the health check was restored to port `8000`.

## 🔗 GitHub Webhook

A GitHub webhook connects the GitHub repository to the local Jenkins server.

When code is pushed to GitHub:

```text
GitHub Push
     ↓
GitHub Webhook
     ↓
Jenkins
     ↓
Pipeline Automatically Starts
```

This removes the need to manually click **Build Now** after every push.

## 🌐 ngrok

ngrok was used to temporarily expose local services to the internet.

### Jenkins Webhook

For GitHub to reach the local Jenkins server:

```text
GitHub
   ↓
ngrok
   ↓
localhost:8080
   ↓
Jenkins
```

### Public Application

ngrok can also expose the application:

```text
Docker Container
       ↓
   localhost:8000
       ↓
      ngrok
       ↓
   Public URL
```

The application was successfully tested through a public ngrok URL.

> **Note:** ngrok URLs are temporary and are intended for development and learning purposes.

## 📊 CI/CD Architecture

```text
                 ┌──────────────┐
                 │   Developer  │
                 └──────┬───────┘
                        │
                        ▼
                 ┌──────────────┐
                 │    GitHub    │
                 └──────┬───────┘
                        │
                    Webhook
                        │
                        ▼
                 ┌──────────────┐
                 │    Jenkins   │
                 └──────┬───────┘
                        │
              ┌─────────┴─────────┐
              │                   │
              ▼                   ▼
        Python Test         Docker Build
              │                   │
              └─────────┬─────────┘
                        │
                        ▼
                 ┌──────────────┐
                 │    Docker    │
                 │   Container  │
                 └──────┬───────┘
                        │
                    Port 8000
                        │
                        ▼
                 ┌──────────────┐
                 │ Health Check │
                 └──────┬───────┘
                        │
                 ┌──────┴──────┐
                 │             │
               PASS          FAIL
                 │             │
                 ▼             ▼
             SUCCESS       ROLLBACK
                               │
                               ▼
                         Previous Image
```

## 🎯 What I Learned

Through this project, I practiced:

* Git and GitHub
* GitHub Webhooks
* Linux and SSH
* Docker images and containers
* Dockerfiles
* Docker port mapping
* Jenkins pipelines
* Jenkins Declarative Pipeline
* CI/CD concepts
* Automated Docker deployment
* Docker image versioning
* Application health checks
* Automatic rollback
* AWS EC2
* Local Jenkins setup
* ngrok tunneling
* Basic DevOps troubleshooting

## 🚀 Future Improvements

* Push Docker images to Docker Hub
* Add automated unit/integration tests
* Add Docker Compose
* Add container monitoring
* Add notifications for failed deployments
* Add a production cloud deployment
* Explore GitHub Actions
* Improve rollback and deployment strategies

## 👨‍💻 Author

**Amruth**

DevOps learning project using **GitHub, Jenkins, Docker, Python, AWS, and ngrok**.
