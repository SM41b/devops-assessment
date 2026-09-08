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
                sh 'python3 -m pytest'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t devops-assessment-api .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose up -d --build api nginx'
            }
        }

        stage('Health Check') {
            steps {
                sh 'for i in 1 2 3 4 5; do curl -f http://nginx/health && exit 0 || sleep 2; done; exit 1'
            }
        }
    }
}