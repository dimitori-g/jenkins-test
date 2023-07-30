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
                sh "python3 -m venv venv"
                // sh "source venv/bin/activate"
                // sh "pip install -r requirements.txt"
                sh """
                    source venv/bin/activate
                    pip install -r requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                sh """
                    source venv/bin/activate
                    pytest
                """
            }

            // post {
            //     always {
            //         sh "deactivate"
            //     }
            // }
        }
    }
}
