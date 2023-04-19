## secrets
secret config file (kind/metadata/type)

Storing the data in a secret component doesn't make it secure as it is plain text. Instead we can use a base 64emcoder (online or [ echo ](https://linuxhint.com/bash_base64_encode_decode/) -n)

```bash
 echo 'linuxhint.com' | base64
# or assign to a value
  B64_VAL="$(echo 'linuxhint.com' | base64)"
```

Just remember that secrets must be configured/exported prior deployment. If referencing a secret that doesn't exist it will crash.

```bash
kubectl apply -f mongo-secret.yaml
# to confirm
kubectl get secret
```

Handy command
```bash
kubectl get all
# or 
kubectl get all | rg mongodb
# again if it takes too long
kubectl describe pod {name of pod}
```

## Internal services

Yaml supports multiple documents nested in the same file. (---)

### service config file
kind(service)
metadata(relevant name)
selector (to connect to pod through label)
ports: port (service port); targetPort (containerPort of Deployment)

reminder that to apply changes you  need to
```bash
kubectl apply -f {same config file}
```

## configMap

External configuration
centralized
Other components can use it (same as secret)

layout of the file:
  kind (configMap); metadata/name (relevant name); data (k:v pairs)

Just like secrets, you must apply the configMap prior the main cluster 

```bash
kubectl apply -f monog-configmap.yaml
```

## services

You can make a service external by:
  passing type: LoadBalancer (but internal service also acts as a loadBalancer)
  nodePort: port for external ip address (usage in browser) must be between 30000-32767

### Minikube mentions
because minikube works differently (internal) we can access the service like such.
```bash
minikube service --url=true mongo-express-service
```
