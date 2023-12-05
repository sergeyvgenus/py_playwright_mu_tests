pipeline {
   agent none
   stages {
        stage('Build the container and run tests') {
            agent {
                dockerfile {
                    args '--ipc=host -v /var/lib/jenkins/workspace/DockerPipeline/tests/allure-reports:/tests/allure-reports'
                }
            }
            steps {
                echo 'Container is build and running'
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'pytest'
            }
        }
    }
    post {
        agent any
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'tests/allure-reports']]
        }
    }
}
//       agent { 
//     dockerfile {
//         args '--ipc=host -v /var/lib/jenkins/workspace/DockerPipeline/tests/allure-reports:/tests/allure-reports'
//     }
//     }
//    stages {
//       stage('Tests') {
//          steps {
//             sh 'python3 --version'
//             sh 'pip3 --version'
//             sh 'pytest'
//          }
//       }
//       stage('Report') {
//         steps {
//             allure includeProperties: false, jdk: '', results: [[path: 'tests/allure-reports']]
//         }
//       }
//    }
// }