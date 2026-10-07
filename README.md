# Docker App – Jenkins CI/CD

A simple DevOps project demonstrating how **GitHub, Jenkins, Docker, AWS EC2, and ngrok** work together to build and deploy a Python web application.

## 📌 Project Overview

This project contains a simple Python web application running inside a Docker container.

### Deployment Flow

```text
Developer
   ↓
GitHub
   ↓
Jenkins
   ↓
Docker Image
   ↓
Docker Container
   ↓
Port 8000
   ↓
ngrok
   ↓
Public Website
```

## 🛠️ Technologies Used

* Git
* GitHub
* Jenkins
* Docker
* Python
* Linux
* AWS EC2
* ngrok

## 📁 Project Structure

```text
docker-app/
│
├── app.py
├── Dockerfile
└── README.md
```

## 🐍 Application

The application is written in Python and runs a simple web server on port `8000`.

## 🐳 Docker

Build the Docker image:

```bash
docker build -t devops-python-app .
```

Run the container:

```bash
docker run -d --name test-app -p 8000:8000 devops-python-app
```

Check the container:

```bash
docker ps
```

Test the application:

```bash
curl http://localhost:8000
```

## 🔧 Jenkins

Jenkins connects to the GitHub repository and builds the Docker image.

The pipeline performs:

```text
1. Clone Repository
2. Build Docker Image
3. Test
```

## 🌍 Public Access with ngrok

ngrok was used to temporarily expose the Docker application to the internet.

```bash
ngrok http 8000
```

The final flow is:

```text
Docker Container
       ↓
   Port 8000
       ↓
     ngrok
       ↓
Public URL
```

The application was successfully tested locally with HTTP `200 OK` and accessed through the public ngrok URL.

> **Note:** The ngrok URL is temporary and intended for development and learning purposes.

## 🎯 What I Learned

Through this project, I practiced:

* Git and GitHub
* Linux and SSH
* Docker images and containers
* Dockerfiles and port mapping
* Jenkins pipelines
* CI concepts
* AWS EC2
* Connecting Jenkins with GitHub
* Building Docker images through Jenkins
* Running and testing a containerized application
* Using ngrok for temporary public access
* Basic DevOps troubleshooting

## 🚀 Future Improvements

* Automate container deployment through Jenkins
* Add automated application testing
* Push Docker images to Docker Hub
* Add GitHub Actions
* Add Docker Compose
* Deploy using a permanent cloud service

## 👨‍💻 Author

**Amruth**

DevOps learning project using AWS, Docker, Jenkins, GitHub, , and ngrok.
