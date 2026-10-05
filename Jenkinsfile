pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t devops-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop devops-app || exit /b 0'
                bat 'docker rm devops-app || exit /b 0'
            }
        }

        stage('Run New Container') {
            steps {
                bat 'docker run -d --name devops-app -p 8000:8000 devops-app'
            }
        }

        stage('Health Check') {
            steps {
                sleep 5
                bat 'curl -f http://localhost:8000'
            }
        }

    }
}
