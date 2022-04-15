# Kubernetes (k8s)
container technology agnostic

node: simple server (virtual/real)
pod: abstraction over container
  Usually one container per pod unless it needs a side-container/helper container
  you normally would prefer a web app and its db to be separated
  each pods gets its own ip where they can communicate with other pods
  beacause the ip would change should e.g. the application db crash kubernetes uses service

service:
  permanent IP address to each pod. The lifecycle of a service is independent of its pod
  2 types: External/internal(not accessible by the public)
ingress:
  because users want to use a dns (domain name service) the request is usually processed through an ingress prior a service
  
configMap: external config of the application (never place .env inside )
secret: just like config map but with the config data (base64 encoded)

Volumes: (for data permanence/just like docker) can be  local/remote(s3). Remember that k8s doesn't manage data persistance.

StatefulSet: for clusters that requires data persistence e.g. db/ Deployment for stateLESS apps 
Dbs are often hosted outside of K8s cluster (stateLESS cluste) and communicate to an elastic db.

### tl:dr main components
Pod (the wrapper around the container)
Service: communication between the pods and outside
Ingress: for the routing of note you can use nginx-ingress
External configuration:
  ConfigMap
  Secrets
Data persistence:
  volume
k8s blueprints
  Deployment: stateLESS
  StatefulSet: a db is attached.

## Basic K8s Architecture
Node (worker nodes)
requires 3 things installed on every node:
  Container runtime (docker, containered, podman?)
  kubelet responsible in taking the container configuration and running a pod with container and allow for ressource allocation. 
  Communication via services
  Kube proxy forwards the request

Master node (usually minimum 2 for redundancy)
requires 4 things:
  api server (cluster gateway/auth)
  scheduler (through the api server) where to put the pod? -> kubelet
  controller manager (detects failures)
  etcd (cluster brain) -> cluster state

There can be multiple master nodes
Add a new MasterNode
  1) get new bare server
  2)install all the master/worker node processes
  3) add it to the cluster

## Minikube
Use-case for localhost testing (master and node running on the same node) running through a virtual machine

## kubectl
interact through minikube through kubectl (cli) which talks to minikube api server.
Kubectl can still be used to interact with ANY k8s node

## install
  


## Trying to move away from dockerfiles

* [ podaman go](https://podman.io/blogs/2020/08/10/podman-go-bindings.html)
* [ containerd ](https://containerd.io/docs/getting-started/)


