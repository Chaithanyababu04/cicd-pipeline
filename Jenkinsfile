pipeline{
    agent any
    stages{
        stage('Build'){
            steps{
                sh 'docker build -t cicd-demo:latest .'
            }
        }
        stage('Test'){
            steps{
                echo 'Testing the application...'
            }
        }
        stage('Deploy'){
            steps{
                sh ''' 
                kubectl delete deployment cicd-app -- ignore-not-found =true
                
                kubectl apply -f deployment.yaml         
                ''' 
        }
    }
}
}
