pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-mohsin')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t project2:latest .'
				sh 'docker tag project2:latest mohsinm/project2:v1'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push mohsinm/project2:v1'
			}
		}

        stage('Pull') {

			steps {
				sh 'docker pull mohsinm/project2:latest'
			}
		}

        stage('Run') {

			steps {
				sh 'docker run -itd --name project2 -p 8080:8080 mohsinm/project2:latest'
			}
		}
	}

	// post {
	// 	always {
	// 		sh 'docker logout'
	// 	}
	// }

}