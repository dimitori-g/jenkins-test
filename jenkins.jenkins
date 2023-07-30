pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/dimitori-g/jenkins-test.git'
            }
        }

        stage('Setup') {
            steps {
                sh "python3 venv venv"
                sh "source venv/bin/activate"
                sh "pip install -r requirements.txt"
            }
        }

        stage('Test') {
            steps {
                sh "pytest"
            }

            post {
                always {
                    sh "deactivate"
                }
            }
        }
    }
}
