cd my_docker_authentification 
docker image build . -t authentification_image:latest

cd ../my_docker_authorization 
docker image build . -t authorization_image:latest

cd ../my_docker_content 
docker image build . -t content_image:latest

#Running of the Docker-compose
docker-compose up 