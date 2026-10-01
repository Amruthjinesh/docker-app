# Python Docker App

This project is a simple Python web server running inside a Docker container.

## 🛠️ Technologies Used

* Python
* Docker
* Linux
* Git
* GitHub

## 📁 Project Structure

```text
docker-app/
├── app.py
├── Dockerfile
└── README.md
```

## 🐍 Python Application

The `app.py` file creates a basic HTTP server using Python's built-in `http.server` module.

The server listens on:

```text
0.0.0.0:8000
```

When a request is received, it returns:

```text
Hello from my DevOps Docker server!
```

## 🐳 Dockerfile

```dockerfile
FROM python:3.14

WORKDIR /app

COPY app.py .

EXPOSE 8000

CMD ["python3", "app.py"]
```

## 🔨 Build Docker Image

Build the Docker image using:

```bash
docker build -t devops-python-app .
```

Check the image:

```bash
docker images
```

## ▶️ Run the Container

```bash
docker run -d --name test-app -p 8000:8000 devops-python-app
```

### Port Mapping

```text
EC2 Host Port 8000
        ↓
Container Port 8000
```

## 🧪 Test the Application

Test from the EC2 server:

```bash
curl http://localhost:8000
```

Expected output:

```text
Hello from my DevOps Docker server!
```

You can also access it from a browser using:

```text
http://<EC2-PUBLIC-IP>:8000
```

Make sure port **8000** is allowed in the EC2 security group.

## 🔍 Useful Docker Commands

Check running containers:

```bash
docker ps
```

Check all containers:

```bash
docker ps -a
```

View container logs:

```bash
docker logs test-app
```

Stop the container:

```bash
docker stop test-app
```

Start the container again:

```bash
docker start test-app
```

Remove the container:

```bash
docker rm test-app
```

Remove the image:

```bash
docker rmi devops-python-app
```

## 🎯 What I Learned

* How to create a simple Python HTTP server
* How to write a Dockerfile
* How to build a Docker image
* How to run a Docker container
* How Docker port mapping works
* How to test a containerized application
* Basic Docker commands
* Running a Python application inside Docker

## 🚀 Project Flow

```text
Python Application
       ↓
    Dockerfile
       ↓
  Docker Image
       ↓
 Docker Container
       ↓
    Port 8000
       ↓
    Web Browser
```
