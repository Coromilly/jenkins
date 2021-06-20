pipeline {
    agent any

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
        stage('Get query') {
            steps {
                echo 'Getting query'
                sh 'mysql -uroot -p1991Darktranqu1ll1ty1991 "shop" < "select.txt"'             
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
                            sourceFile: '', 
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
