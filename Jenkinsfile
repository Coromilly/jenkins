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
                sh "pwd"
                sh "ls -la"                
            }
        }
        // stage('Create bucket') {
        //     steps {
        //         echo 'Creating Bucket'
        //         sh "aws s3api create-bucket --bucket levdansky-bucket-from-jenkins"               
        //     }
        }
        stage('Upload Files') {
            steps {
                echo 'Uoloading files'
                s3Upload consoleLogLevel: 'INFO', 
                dontSetBuildResultOnFailure: false, 
                dontWaitForConcurrentBuildCompletion: false, 
                entries: 
                [
                    [bucket: 'levdansky-bucket-from-jenkins', 
                    excludedFile: '.git, Jenkinsfile', 
                    flatten: false, 
                    gzipFiles: false, 
                    keepForever: false, 
                    managedArtifacts: false, 
                    noUploadOnFailure: false, 
                    selectedRegion: 'us-east-1', 
                    showDirectlyInBrowser: false, 
                    sourceFile: '', 
                    storageClass: 'STANDARD', 
                    uploadFromSlave: false, 
                    useServerSideEncryption: false]
                ], 
                pluginFailureResultConstraint: 'FAILURE', 
                profileName: '', 
                userMetadata: []            }
        }
    }
}
