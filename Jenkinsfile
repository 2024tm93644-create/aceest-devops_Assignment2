pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-app:v1 .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                sh 'docker run aceest-app:v1 python -m pytest'
            }
        }
    }
}