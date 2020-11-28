pipeline {
    agent { dockerfile true }
    stages {
        stage('Stage 1 - Check Python version') {
            steps {
                sh 'python --version'
            }
        }
        stage('Stage 2 - Run hello world') {
            steps {
                sh 'python src/app.py'
            }
        }
    }
}