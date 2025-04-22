pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'coffee-dashboard'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m pytest tests/'
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh '''
                        docker-compose down
                        docker-compose up -d
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}