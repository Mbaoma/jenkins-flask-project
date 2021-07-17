pipeline {
   agent { docker {image 'python:3.7.2'  } }
    stages {
        stage('build') {
            steps {
                sh 'sh virtualenv venv && . venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('test') {
            steps {
                sh 'python -m unittest discover'
            }
        }
        stage('deploy') {
            steps {
                sh 'python app/main.py'
            }
        }
    }
}