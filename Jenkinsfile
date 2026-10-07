pipeline {
    agent any

    environment {
        IMAGE_NAME = "devops-app"
        IMAGE_TAG = "build-${BUILD_NUMBER}"
    }

    stages {

        stage('Test') {
            steps {
                bat 'docker run --rm -v "%CD%:/app" -w /app python:3.14 python -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%IMAGE_TAG% .'
            }
        }

        stage('Save Previous Image') {
            steps {
                script {
                    def previousImage = bat(
                        script: '@docker inspect --format="{{.Config.Image}}" devops-app',
                        returnStdout: true
                    ).trim()

                    env.PREVIOUS_IMAGE = previousImage

                    echo "Previous image: ${env.PREVIOUS_IMAGE}"
                }
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
                bat 'docker run -d --name devops-app -p 8000:8000 %IMAGE_NAME%:%IMAGE_TAG%'
            }
        }

        stage('Health Check') {
            steps {
                sleep 5
                bat 'curl -f http://localhost:8000'
            }
        }
    }

    post {
        failure {
            script {
                if (env.PREVIOUS_IMAGE) {
                    echo "Deployment failed!"
                    echo "Rolling back to: ${env.PREVIOUS_IMAGE}"

                    bat 'docker stop devops-app || exit /b 0'
                    bat 'docker rm devops-app || exit /b 0'

                    bat 'docker run -d --name devops-app -p 8000:8000 %PREVIOUS_IMAGE%'

                    echo "Rollback completed."
                }
            }
        }
    }
}
