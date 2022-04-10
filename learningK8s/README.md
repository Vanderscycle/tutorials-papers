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

Volumes: (for data permanence/just like docker) can be  local/remote(s3)

[bookmark](https://youtu.be/X48VuDVv0do?t=1103)


## Trying to move away from dockerfiles

* [ podaman go](https://podman.io/blogs/2020/08/10/podman-go-bindings.html)
* [ containerd ](https://containerd.io/docs/getting-started/)


