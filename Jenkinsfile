pipeline {
    agent any
    environment {
        MYSQL_CREDS = credentials('3')
    }

    stages {
        stage('Pull Repository') {
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
        stage('Backup database') {
            steps {
                echo 'Make backup'
                sh 'mysqldump -u$MYSQL_CREDS_USR -p$MYSQL_CREDS_PSW shop > backup.sql'             
            }
        }
        stage('Upload backup') {
            steps {
                echo 'Uploading backup'
                s3Upload consoleLogLevel: 'WARNING', 
                dontSetBuildResultOnFailure: false, 
                dontWaitForConcurrentBuildCompletion: false, 
                entries: 
                    [
                        [
                            bucket: 'levdansky-bucket-from-jenkins', 
                            excludedFile: '.git, Jenkinsfile', 
                            flatten: false, 
                            gzipFiles: false, 
                            keepForever: false, 
                            managedArtifacts: false, 
                            noUploadOnFailure: true, 
                            selectedRegion: 'us-east-1', 
                            showDirectlyInBrowser: false, 
                            sourceFile: 'backup.sql', 
                            storageClass: 'STANDARD', 
                            uploadFromSlave: false, 
                            useServerSideEncryption: false
                        ]
                    ], 
                pluginFailureResultConstraint: 'FAILURE', 
                profileName: 'S3_jenkins', 
                userMetadata: []
            }
        }
        stage('Get query') {
            steps {
                echo 'Getting query'
                sh 'mysql -uroot -p1991Darktranqu1ll1ty1991 shop < select.txt > result.txt'             
            }
        }
        stage('Upload Files') {
            steps {
                echo 'Uploading files'
                s3Upload consoleLogLevel: 'WARNING', 
                dontSetBuildResultOnFailure: false, 
                dontWaitForConcurrentBuildCompletion: false, 
                entries: 
                    [
                        [
                            bucket: 'levdansky-bucket-from-jenkins', 
                            excludedFile: '.git, Jenkinsfile', 
                            flatten: false, 
                            gzipFiles: false, 
                            keepForever: false, 
                            managedArtifacts: false, 
                            noUploadOnFailure: true, 
                            selectedRegion: 'us-east-1', 
                            showDirectlyInBrowser: false, 
                            sourceFile: 'result.txt', 
                            storageClass: 'STANDARD', 
                            uploadFromSlave: false, 
                            useServerSideEncryption: false
                        ]
                    ], 
                pluginFailureResultConstraint: 'FAILURE', 
                profileName: 'S3_jenkins', 
                userMetadata: []
            }
        }
    }
}
