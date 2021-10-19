pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat """
                docker build -t hello .
                """
            }
        }
        stage('Run') {
           steps {
                bat """
                docker run --rm hello
                """
            }
        
        }     

    }
}
