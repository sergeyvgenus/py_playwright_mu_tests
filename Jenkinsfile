pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.39.0-jammy' } }
   stages {
      stage('Tests') {
         steps {
            sh 'python3 --version'
            sh 'pip3 --version'
            sh 'pip3 install -r requirements.txt'
            sh 'python3 -m pip install --upgrade pip'
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