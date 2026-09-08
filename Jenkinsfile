pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm -v "$PWD":/app -w /app python:3.12-slim bash -c "pip install -r requirements.txt && pip install pytest httpx && python -m pytest"'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t devops-assessment-api .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose up -d --build'
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl -f http://nginx/health'
            }
        }
    }
}