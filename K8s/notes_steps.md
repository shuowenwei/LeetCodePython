- refer to https://www.youtube.com/watch?v=s_o8dwzRlu4&t=1130s starting from ```Kubernetes Configuration``` 

## Setup

- run ```brew install minikube``` to install minukube, run ```which minikube``` to check 
installation status 
- start docker desktop (or install first it from https://docs.docker.com/desktop/install/mac-install/)
- run ```minikube start --driver docker```, check status ```minikube status```
- run ```kubectl get node``` to see "control-place, master"


## Demo Project Overview

download files from https://gitlab.com/nanuchi/k8s-in-1-hour

For ```mongo-secret.yaml```:
- run ```echo -n mongouser | base64``` to get ```bW9uZ291c2Vy``` 
- run ```echo -n mongoupassword | base64``` to get ```bW9uZ29wYXNzd29yZA==``` 

After 4 yaml files are created 
- run ```kubectl get pod``` should get nothing back 
- ConfigMap and Secret must exist before Deployments, run ```kubectl apply -f mongo-config.yaml``` and ```kubectl apply -f mongo-secret.yaml```
- then create mongdb before webapp, run ```kubectl apply -f mongo.yaml```
- last create webapp, run ```kubectl apply -f webapp.yaml```

## Check status: 
- run ```kubectl get all``` and get:
```
(base) C02YW93VLVCG:~ k26609$ kubectl get all
NAME                                     READY   STATUS    RESTARTS   AGE
pod/mongo-deployment-7d4d5c9f6c-mrb4c    1/1     Running   0          75s
pod/webapp-deployment-649d7fb885-2jcg4   1/1     Running   0          47s

NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP          78m
service/mongo-service    ClusterIP   10.98.74.86      <none>        27017/TCP        75s
service/webapp-service   NodePort    10.108.172.149   <none>        3000:30100/TCP   47s

NAME                                READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/mongo-deployment    1/1     1            1           75s
deployment.apps/webapp-deployment   1/1     1            1           47s

NAME                                           DESIRED   CURRENT   READY   AGE
replicaset.apps/mongo-deployment-7d4d5c9f6c    1         1         1       75s
replicaset.apps/webapp-deployment-649d7fb885   1         1         1       47s
```
- try ```kubectl get configmap```
- try ```kubectl get secret```
- try ```kubectl get pod```
- try ```kubectl --help```, ```kubectl get --help``` and ```kubectl xxx  --help```
- try ```kubectl get pod```
- to see more details about something: ```kubectl describe service webapp-service```, or ```kubectl describe pod webapp-deployment-649d7fb885-2jcg4``` 
- to see logs and stream it, run ```kubectl logs webapp-deployment-649d7fb885-2jcg4 -f```

## access the service from web
- To see all the services ```kubectl get svc``` 
- See to the minicube IP ```minikube ip``` or ```kubectl get node -o wide```
- From browser ```http://192.168.49.2:30100/```

## terminate K8S
refer to https://minikube.sigs.k8s.io/docs/start/
- Pause Kubernetes without impacting deployed applications: ```minikube pause```
- Unpause a paused instance: ```minikube unpause```
- Halt the cluster: ```minikube stop```
- Increase the default memory limit (requires a restart): ```minikube config set memory 16384```
- Browse the catalog of easily installed Kubernetes services: ```minikube addons list```
- Create a second cluster running an older Kubernetes release: ```minikube start -p aged --kubernetes-version=v1.16.1```
- Delete all of the minikube clusters: ```minikube delete --all```
