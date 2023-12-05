pipeline {
   agent { 
    dockerfile {
        args '--ipc=host -v /var/lib/jenkins/workspace/DockerPipeline/tests/allure-reports:/tests/allure-reports'
    }
    }
   stages {
      stage('Tests') {
         steps {
            sh 'python3 --version'
            sh 'pip3 --version'
            sh 'pytest'
         }
      }
      stage('Report') {
        steps {
            allure includeProperties: false, jdk: '', results: [[path: 'tests/allure-reports']]
        }
      }
   }
}