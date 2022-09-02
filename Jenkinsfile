pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-mohsin') // Dockerhub profile name
	}
	
	stages {

		stage('Build') { //Build the docker locally and tagged it with version 

			steps {
				sh 'docker build -t project2:latest .'
				sh 'docker tag project2:latest mohsinm/project2:v2'
			}
		}

		stage('Login') { //Login to dockerhub  to push the built image. 

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') { // Docker image is then pushed to Dockerhub repository

			steps {
				sh 'docker push mohsinm/project2:v2'
			}
		}

        stage('Pull') { // Docker Image is pulled back to be built again

			steps {
				sh 'docker pull mohsinm/project2:v2'
			}
		}

		stage('Stop') { // Previous running container is stopped and removed

			steps {
				sh 'docker ps -f name=project2 -q | xargs --no-run-if-empty docker container stop'
				sh 'docker container ls -a -fname=project2 -q | xargs -r docker container rm'
			}
		}

        stage('Run') { // Docker Container run using the Dockerhub Image pulled in previous stage

			steps {
				sh 'docker run -itd --name project2 -p 8080:8080 mohsinm/project2:v2'
			}
		}
	}

	
}