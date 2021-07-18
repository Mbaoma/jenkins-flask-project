pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.jenkinsAgent'
            additionalBuildArgs  '--build-arg JENKINSUID=`id -u jenkins` --build-arg JENKINSGID=`id -g jenkins` --build-arg DOCKERGID=`stat -c %g /var/run/docker.sock`'
            args '-v /var/run/docker.sock:/var/run/docker.sock -u jenkins:docker'
        }
    }
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