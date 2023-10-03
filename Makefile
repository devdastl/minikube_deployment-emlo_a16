USERNAME = default
PROJECT = emlo
TAG = assignment16-v1

#setup make commands
help:
	@echo "Makefile supported commands:"
	@echo "build-image: Build image from Dockerfile"
	@echo "start-minikube: Run docker container in interactive mode"
	@echo "run-train: Run training on default config"

start-minikube:
	@echo "starting minikube on docker"
	minikube start --driver=docker

build-image:
	@echo "building docker image for CLIP service"
	docker build -t ${USERNAME}/${PROJECT}:${TAG} .

push-to-minikube:
	@echo "pushing image to minikube"
	minikube image load ${USERNAME}/${PROJECT}:${TAG}

start-deployment:
	@echo "Building and deploying CLIP service"
	minikube kubectl -- apply -f deployment_config

start-tunnel:
	@echo "Starting minikube tunnel"
	minikube tunnel
