# Docker Images

## For removing orphan, closed, containers
remove:
	sudo docker-compose down --remove-orphans

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

build-server-crowd-sourced:
	docker-compose build --no-cache server

build-client-crowd-sourced:
	docker-compose build --no-cache client

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
	sudo docker exec -it server-crowd-sourced /bin/bash

client:
	sudo docker exec -it client-crowd-sourced /bin/bash

precommit:
	flake8 server && black server

gen-data:
	@ sudo chmod +x server/scripts/generate_json.sh
	@ bash ./server/scripts/generate_json.sh ./server/shared/img/Tripix ./server/shared/json/Tripix

save-gen-data-to-db:
	sudo chmod +x scripts/save-gen-data-to-db.sh
	./scripts/save-gen-data-to-db.sh
	
# download datasets
datasets-download:
	chmod +x scripts/datasets-download.sh
	./scripts/datasets-download.sh

# process and move datasets to the right folders
datasets-setup:
	chmod +x scripts/datasets-setup.sh
	./scripts/datasets-setup.sh
