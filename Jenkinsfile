pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "django-docker-jenkins-app"
        DOCKER_REGISTRY = "index.docker.io"  // Replace with your Docker registry
        DOCKER_CREDENTIALS = credentials('docker-credentials')  // Jenkins credentials ID
        DB_NAME = 'jktechnologies_db'
        DB_USER = credentials('db-user-credential-id')
        DB_PASSWORD = credentials('db-password-credential-id')
    }
    }
    stages {
        stage('Create .env File') {
            steps {
                script {
                    // Write environment variables to .env file
                    sh '''
                        echo "DB_NAME=${DB_NAME}" > .env
                        echo "DB_USER=${DB_USER}" >> .env
                        echo "DB_PASSWORD=${DB_PASSWORD}" >> .env
                    '''
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml build'
                }
            }
        }
        stage('Push to Registry') {
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REGISTRY}", DOCKER_CREDENTIALS) {
                        sh "docker-compose -f docker-compose.yml push"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml down'
                    sh 'docker-compose -f docker-compose.yml up -d'
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
