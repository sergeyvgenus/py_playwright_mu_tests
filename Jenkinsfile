pipeline {
   agent { dockerfile true }
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