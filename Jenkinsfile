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
                sh 'python -m pytest'
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