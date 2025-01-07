pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                echo 'Building the application'
                sh 'echo Running build commands...'
            }
        }

        stage("Test") {
            steps {
                echo 'Testing the application'
                sh 'echo Running tests...'
            }
        }

        stage("Deploy") {
            steps {
                echo 'Deploying the application'
                sh 'echo Deploying to server...'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
    }
}
