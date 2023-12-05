pipeline {
    agent any
    stages {
        stage('Build the container and run tests') {
            agent {
                dockerfile {
                    args '--ipc=host -v /var/lib/jenkins/workspace/DockerPipeline@2/tests/allure-reports:/tests/allure-reports'
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
        always {
            allure includeProperties: false, jdk: '', results: [[path: '/var/lib/jenkins/workspace/DockerPipeline@2/tests/allure-reports']]
        }
    }
}
    

// pipeline {

//     agent { 
//         dockerfile {
//             args '--ipc=host -v /var/lib/jenkins/workspace/DockerPipeline/tests/allure-reports:/tests/allure-reports'
//         }
//     }
//     stages {
//         stage('Tests') {
//             steps {
//                 echo 'Running tests'
//                 sh 'python3 --version'
//                 sh 'pip3 --version'
//                 sh 'pytest'
//             }
            
//             post {
//                 always {
//                     allure includeProperties: false, jdk: '', results: [[path: 'tests/allure-reports']]
//                 }
//             }
//         }
//     }
// }
