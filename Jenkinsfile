pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                sh 'python -m nittest discover'
            }
        }
        stage('deploy') {
            steps {
                sh 'python app/main.py'
            }
        }
    }
}