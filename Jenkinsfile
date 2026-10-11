pipeline {
    agent { label 'deployagent' }

    environment {
        IMAGE_NAME = "devops-app"
        IMAGE_TAG = "build-${BUILD_NUMBER}"
    }

    stages {

        stage('Test') {
            steps {
                sh 'docker run --rm -v "$WORKSPACE:/app" -w /app python:3.14 python -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Save Previous Image') {
            steps {
                script {
                    def prev = sh(
                        script: "docker inspect --format='{{.Config.Image}}' devops-app 2>/dev/null || true",
                        returnStdout: true
                    ).trim()
                    env.PREVIOUS_IMAGE = prev
                    echo "Previous image: ${prev ?: 'none'}"
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop devops-app || true'
                sh 'docker rm devops-app || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name devops-app -p 8000:8000 $IMAGE_NAME:$IMAGE_TAG'
            }
        }

        stage('Health Check') {
            steps {
                sleep 5
                sh 'curl -f http://localhost:8001'
            }
        }
    }

    post {
        failure {
            script {
                if (env.PREVIOUS_IMAGE) {
                    echo "Rolling back to: ${env.PREVIOUS_IMAGE}"
                    sh 'docker stop devops-app || true'
                    sh 'docker rm devops-app || true'
                    sh 'docker run -d --name devops-app -p 8000:8000 $PREVIOUS_IMAGE'
                }
            }
        }
    }
}