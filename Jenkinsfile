pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat """
                docker build -t hello_there .
                """
            }
        }
        stage('Run') {
           steps {
                bat """
                docker run --rm hello_there
                """
            }
        
        }     

    }
}
