# minikube_deployment-emlo_a16
This is 16th assignment of course EMLO from TSAI.

## Introduction
This assignment/project focuses on using Minikube to create a single node deployment locally. Here we are using FastAPI to deploy a CLIP service on `/clip-inference` route.
## Prerequisite
Below are some prerequisite required:
- Optional: Docker installed to use as driver for minikube.
- Required: Minikube installed 
- Required: Addons `minikube addons enable ingress` & `minikube addons server-metrice`
- Required: Make CLI
## Getting started
This repository uses Makefile to run the command easier. 
</br>
Below are the steps which can be followed to start the deployment.
1. Start minikube cluster: By running `make start-minikube`. This will start the cluster.
2. Builddocker image: for FASTAPI server. Run `make build-image`. Source code is in `src/` dir.
3. Push docker image: to minikube registory. Run `make push-to-minikube`. This will push the image to minikube isolated registory.
4. Start deployment: By running `make start-deployment`. This will start the deployment based on yaml files in `deployment_config/`.
5. Start tunnel by `minikube tunnel` and access the service on `clip.localhost/docs`
6. Make sure that everything is working. `kubectl get all`.

## Using service via swagger

