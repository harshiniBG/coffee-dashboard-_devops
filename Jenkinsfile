pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'coffee-dashboard'
    }

    triggers {
        pollSCM('H/5 * * * *') // Check for changes every 5 minutes
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m pytest tests/ --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
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
        failure {
            emailext body: 'Build failed: ${BUILD_URL}',
                    subject: 'FAILED: ${JOB_NAME} - Build #${BUILD_NUMBER}',
                    to: 'dev-team@example.com'
        }
        success {
            emailext body: 'Build succeeded: ${BUILD_URL}',
                    subject: 'SUCCESS: ${JOB_NAME} - Build #${BUILD_NUMBER}',
                    to: 'dev-team@example.com'
        }
    }
}
