#!/bin/bash

kubectl create -f timer/depl/tm_service.yaml
kubectl create -f timer/depl/server_depl.yaml 
kubectl create -f timer/depl/pinger_depl.yaml

minikube tunnel
