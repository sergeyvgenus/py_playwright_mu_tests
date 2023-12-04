pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.39.0-jammy' } }
   stages {
      stage('Tests') {
         steps {
            sh 'pip install -r requirements.txt'
            sh 'python -m pip install --upgrade pip'
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