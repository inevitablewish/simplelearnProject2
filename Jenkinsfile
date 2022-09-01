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

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push project2:latest'
			}
		}

        stage('Pull') {

			steps {
				sh 'docker pull project2:latest'
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