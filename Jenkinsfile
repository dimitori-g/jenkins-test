pipeline {
    agent any

    environment {
        // Define the Python version to use
        PYTHON_VERSION = '3.8'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from version control
                // For example, if you're using Git:
                git 'https://github.com/dimitori-g/jenkins-test.git'
            }
        }

        stage('Setup') {
            steps {
                // Install Python and create a virtual environment
                sh "pyenv install ${PYTHON_VERSION}"
                sh "pyenv virtualenv ${PYTHON_VERSION} venv"
                sh "pyenv local venv"
                sh "pip install -r requirements.txt"
            }
        }

        stage('Test') {
            steps {
                // Run pytest
                sh "pytest"
            }

            post {
                always {
                    // Deactivate the virtual environment
                    sh "pyenv deactivate"
                }
            }
        }
    }
}
