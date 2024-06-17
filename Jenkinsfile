pipeline {
    agent any // windows agent, Jenkins-Laravel (other machine)
    
    stages {
        stage('Fetch from GitHub') { // build steps
            steps {
                echo 'Fetching from GitHub'
                git branch: 'main', url:'https://github.com/Leangkimlong/Laravel-jenkins.git'
            }
        }
        stage('Install Composer') {
            steps {
                sh 'composer install'
            }
        }
        stage('install npm') {
            steps {
                sh 'npm i'
                sh 'npm run build'
            }
        }
        stage('Generate Key'){
            steps{
                sh 'php artisan key:generate'
            }
        }
    }
}