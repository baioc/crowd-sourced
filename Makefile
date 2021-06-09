stop:
	docker container stop $(docker ps -q)

delete:
	docker container rm $(docker ps -q)

remove:
	sudo docker-compose down --remove-orphans

# Building Docker Images

## For Docker Compose, Production
build-prod:
	sudo docker-compose -f docker-compose.yaml up --build

## For Docker Compose, Development
build-dev:
	sudo chmod +x scripts/build-dev.sh
	./scripts/build-dev.sh

## For building only server image
build-server:
	sudo chmod +x scripts/build-server.sh
	./scripts/build-server.sh

## For building only client image
build-client:
	sudo chmod +x scripts/build-client.sh
	./scripts/build-client.sh	

# Starting Docker Images

## For Docker Comppose, Production
up-prod:
	sudo docker-compose -f docker-compose.yaml up

## For Docker Comppose, Development
up-dev:
	sudo docker-compose -f docker-compose.dev.yaml up

## For starting only server image
up-server:
	sudo chmod +x scripts/up-server.sh
	./scripts/up-server.sh

## For starting only client iamge
up-client:
	sudo chmod +x scripts/up-client.sh
	./scripts/up-client.sh	

# List all process
ps:
	sudo docker-compose ps -a

# List all images
images:
	sudo docker images

server:
	sudo docker exec -it server-findex /bin/bash

client:
	sudo docker exec -it client-findex /bin/bash