pipeline {
    agent any

    environment {
        // Define the path to the virtual environment
        VIRTUAL_ENV = "${WORKSPACE}/venv"
        PATH = "${VIRTUAL_ENV}/bin:${PATH}"
    }
    stages {
        stage('Clone') {
            steps {
               git branch: 'Python', url: 'https://github.com/Leangkimlong/Laravel-jenkins.git'
            }
        }
        stage('Install Python 3 and pip') {
            steps {
                script {
                    sh 'apt-get update'
                    sh 'apt-get install -y python3 python3-pip'
                }
            }
        }
        stage('Setup') {
            steps {
                script {
                    // Create a virtual environment
                    sh "python3 -m venv ${VIRTUAL_ENV}"
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Activate the virtual environment and install pytest
                    sh "${VIRTUAL_ENV}/bin/pip install pytest"
                }
            }
        }
        stage('Build') {
            steps {
                sh 'python3 operation.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
    
    post{
       success {
            emailext subject: 'Jenkins Build Successful',
                      body: 'Your Jenkins build succeeded. Congratulations!',
                      to: 'mizterlong95@gmail.com',
                      from: 'jenkins@example.com'
        }
        failure {
            emailext subject: 'Jenkins Build Failed',
                      body: 'Your Jenkins build failed. Please investigate.',
                      to: 'mizterlong95@gmail.com',
                      from: 'jenkins@example.com'
        }
    }
}