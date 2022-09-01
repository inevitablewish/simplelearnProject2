pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-mohsin')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t project2:latest .'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push mohsinm/project2:latest'
			}
		}

        stage('Pull') {

			steps {
				sh 'docker pull mohsinm/project2:latest'
			}
		}

        stage('Run') {

			steps {
				sh 'docker run -itd --name project2 -p 8080:8080 project2:latest'
			}
		}
	}

	// post {
	// 	always {
	// 		sh 'docker logout'
	// 	}
	// }

}