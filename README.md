# Docker App – Jenkins CI/CD

A simple DevOps project demonstrating how **GitHub, Docker, and Jenkins** work together to build and test a Python application.

## 📌 Project Overview

This project contains a simple Python web application that runs inside a Docker container.

The workflow is:

```text
Developer
   ↓
GitHub
   ↓
Jenkins
   ↓
Clone Repository
   ↓
Build Docker Image
   ↓
Run/Test Application
```

## 🛠️ Technologies Used

* Git
* GitHub
* Jenkins
* Docker
* Python
* Linux
* AWS EC2

## 📁 Project Structure

```text
docker-app/
│
├── app.py
├── Dockerfile
└── README.md
```

## 🐍 Application

The application is written in Python and starts a simple HTTP server on port `8000`.

Example response:

```text
Hello from my DevOps Docker server!
```

## 🐳 Dockerfile

The Dockerfile is used to create the application image.

```dockerfile
FROM python:3.14

WORKDIR /app

COPY app.py .

EXPOSE 8000

CMD ["python3", "app.py"]
```

## ▶️ Run Without Docker

You can run the application directly with Python:

```bash
python3 app.py
```

Then test it:

```bash
curl http://localhost:8000
```

Expected output:

```text
Hello from my DevOps Docker server!
```

## 🐳 Run With Docker

Build the Docker image:

```bash
docker build -t devops-python-app .
```

Run the container:

```bash
docker run -d --name test-app -p 8000:8000 devops-python-app
```

Check running containers:

```bash
docker ps
```

Test the application:

```bash
curl http://localhost:8000
```

Stop the container:

```bash
docker stop test-app
```

Remove the container:

```bash
docker rm test-app
```

## 🔧 Jenkins

Jenkins is running separately from the GitHub repository.

Jenkins connects to the GitHub repository and performs the CI process.

### Jenkins Pipeline

The pipeline performs these steps:

```text
1. Clone
2. Build Docker Image
3. Test
```

Example Jenkins pipeline:

```groovy
pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/Amruthjinesh/docker-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-python-app .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker images'
                sh 'echo Docker build completed successfully'
            }
        }
    }
}
```

## 🔄 GitHub → Jenkins

GitHub stores the source code.

Jenkins does **not** need to be inside the GitHub repository.

Instead:

```text
GitHub Repository
       │
       │ git clone
       ↓
    Jenkins
       │
       ↓
 Docker Build
       │
       ↓
 Docker Image
```

## ☁️ AWS EC2

The project is hosted and tested on an AWS EC2 Ubuntu instance.

Jenkins and Docker are installed on the EC2 server.

Useful commands:

```bash
docker ps
```

```bash
docker images
```

```bash
docker ps -a
```

```bash
systemctl status docker
```

## 🎯 What I Learned

Through this project, I practiced:

* Linux commands
* Git and GitHub
* GitHub repositories
* Git branches
* SSH authentication
* Docker images
* Docker containers
* Dockerfiles
* Port mapping
* Jenkins
* Jenkins pipelines
* CI concepts
* AWS EC2
* Connecting Jenkins with GitHub
* Building Docker images automatically

## 🚀 Future Improvements

Possible next steps:

* Add automatic Jenkins builds when code is pushed to GitHub
* Add automated application testing
* Push Docker images to Docker Hub
* Deploy the container automatically
* Add GitHub Actions
* Add Docker Compose
* Add a Jenkins CI/CD pipeline

## 👨‍💻 Author

**Amruth**

DevOps learning project using AWS, Docker, Jenkins and GitHub.
