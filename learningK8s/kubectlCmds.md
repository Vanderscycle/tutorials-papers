Start the localhost env
kubetcl: from minikube to production cluster management
Minikube: start/delete localclusters
```bash
minikube start #--vm-drive=hyperkit/virtualbox
```

Get all running node status
```bash
kubectl get nodes
kubectl get pod 
kubectl get services
```

In the K8s world you do not create pods manually as they are the smallest unit but you create deployments - abstraction over pods
create a new
```bash
kubectl create deployment NAME --image=image [--dry-run] [options]
```
view the deployment
```bash
kubectl get deployment
```
example
```bash
kubetctl create deployment nginx-depl --image=nginx
```
get all the replicas created from one image (shouldn't have to touch this)
```bash
kubectl get replicaset
```
Get/edit the config file of the stateLESS deployment
```bash
kubectl edit deployment nginx-depl
```

## debugging
just like docker you can get the logs
```bash
kubectl logs {pod name} # use get pods
```
sometimes you just don't know what is going on and the logs aren't clear
```bash
kubectl describe pods {pod name}
```
log inside
```bash
kubectl exec -it {pod name} -- bin/bash
```
## delete 
```bash
kubectl delete deployment {pod name}
```

## create from config (yml)
```bash
kubectl apply -f {file_name} 
```



