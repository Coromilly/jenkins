pipeline {
    agent any

    stages {
        stage('Pull repository') {
            steps {
                echo 'Pulling repo'
                checkout(
                    [
                        $class: 'GitSCM', 
                        branches: [[name: '*/master']], 
                        extensions: [], 
                        userRemoteConfigs: [[credentialsId: 'a0369113-b9da-4fd5-8f6b-f5c554fcf56c', url: 'https://github.com/Coromilly/jenkins.git']]
                    ]
                )                               
            }
        }
        stage('Build image') {
            steps {
                echo 'Build image'
                sh 'docker build -t coromilly/task4 .'             
            }
        }
        stage('Push image') {
            steps {
                echo 'Pushing image to dockerhub'
                withDockerRegistry([credentialsId: '10', url: '']) {
                    sh 'docker push coromilly/task4'
                }             
            }
        }
    }
}
