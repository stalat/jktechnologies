pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "django-docker-jenkins-app"
        DOCKER_REGISTRY = "index.docker.io"
        DB_NAME = 'jktechnologies_db'
        DB_USER = credentials('db-user-credential-id')
        DB_PASSWORD = credentials('db-password-credential-id')
        DB_HOST = 'postgres_db'
        DB_PORT = '5432'
    }
    stages {
        stage('Create .env File') {
            steps {
                script {
                    // writing environment variables to dynamically generated .env file
                    sh '''
                        echo "DB_NAME=${DB_NAME}" > .env
                        echo "DB_USER=${DB_USER}" >> .env
                        echo "DB_PASSWORD=${DB_PASSWORD}" >> .env
                        echo "DB_HOST=${DB_HOST}" >> .env
                        echo "DB_PORT=${DB_PORT}" >> .env
                    '''
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml build'
                    sh 'docker-compose -f docker-compose.yml up -d'
                }
            }
        }
        stage('Push to Registry') {
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REGISTRY}", 'docker-credentials') {
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
