# minikube_deployment-emlo_a16
This is 16th assignment of course EMLO from TSAI.

## Introduction
## Prerequisite
## Getting started
This repository uses Makefile to run the command easier. 
</br>
Below are the steps which can be followed to start the deployment.
1. Start minikube cluster: By running `make start-minikube`. This will start the cluster.
2. Builddocker image: for FASTAPI server. Run `make build-image`. Source code is in `src/` dir.
3. Push docker image: to minikube registory. Run `make push-to-minikube`. This will push the image to minikube isolated registory.
4. Start deployment: By running `make start-deployment`. This will start the deployment based on yaml files in `deployment_config/`.
5. Make sure that everything is working. `kubectl get all`.
