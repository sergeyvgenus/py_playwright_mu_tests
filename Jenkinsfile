pipeline {

    agent { 
        dockerfile {
            args '--ipc=host -v /var/lib/jenkins/workspace/DockerPipeline/tests/allure-results:/tests/allure-results'
        }
    }
    stages {
        stage('Tests') {
            steps {
                echo 'Running tests'
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pytest'
            }
            
            post {
                always {
                    allure includeProperties: false, jdk: '', report: 'tests/allure-results', results: [[path: 'tests/allure-report']]
                }
            }
        }
    }
}
