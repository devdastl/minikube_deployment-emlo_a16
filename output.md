Here are some console output of certain command.
1. #### `kubectl describe deployment clip-deployment` console output
```
Name:                   clip-deployment
Namespace:              default
CreationTimestamp:      Tue, 03 Oct 2023 15:23:09 +0530
Labels:                 app=clip
Annotations:            deployment.kubernetes.io/revision: 1
Selector:               app=clip
Replicas:               2 desired | 2 updated | 2 total | 2 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app=clip
  Containers:
   clip-inference:
    Image:        default/emlo:assignment16-v1
    Port:         7860/TCP
    Host Port:    0/TCP
    Environment:  <none>
    Mounts:       <none>
  Volumes:        <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Available      True    MinimumReplicasAvailable
  Progressing    True    NewReplicaSetAvailable
OldReplicaSets:  <none>
NewReplicaSet:   clip-deployment-67b6d9c849 (2/2 replicas created)
Events:
  Type    Reason             Age   From                   Message
  ----    ------             ----  ----                   -------
  Normal  ScalingReplicaSet  80s   deployment-controller  Scaled up replica set clip-deployment-67b6d9c849 to 2
```

2. #### `kubectl describe pod clip-deployment-67b6d9c849-9l988`  console output
```
Name:             clip-deployment-67b6d9c849-9l988
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Tue, 03 Oct 2023 15:23:09 +0530
Labels:           app=clip
                  pod-template-hash=67b6d9c849
Annotations:      <none>
Status:           Running
IP:               10.244.0.3
IPs:
  IP:           10.244.0.3
Controlled By:  ReplicaSet/clip-deployment-67b6d9c849
Containers:
  clip-inference:
    Container ID:   docker://fd4460f3a33884cf7285aa654b9c9dc689a4f8215b2fb6423ba313ddef0ff56b
    Image:          default/emlo:assignment16-v1
    Image ID:       docker://sha256:a666ec22f5c376710f7821fed118594c5004153d42af137922ebe12f15fb6c16
    Port:           7860/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 03 Oct 2023 15:23:12 +0530
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-wqh2k (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-wqh2k:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  4m34s  default-scheduler  Successfully assigned default/clip-deployment-67b6d9c849-9l988 to minikube
  Normal  Pulled     4m32s  kubelet            Container image "default/emlo:assignment16-v1" already present on machine
  Normal  Created    4m32s  kubelet            Created container clip-inference
  Normal  Started    4m31s  kubelet            Started container clip-inference
```

3. #### `kubectl describe ingress clip-ingress` console output
```
Name:             clip-ingress
Labels:           <none>
Namespace:        default
Address:          
Ingress Class:    <none>
Default backend:  <default>
Rules:
  Host            Path  Backends
  ----            ----  --------
  clip.localhost  
                  /   clip-service:80 (10.244.0.3:80,10.244.0.4:80)
Annotations:      <none>
Events:           <none>
```
4. #### `kubectl top pod` console output
```
NAME                               CPU(cores)   MEMORY(bytes)   
clip-deployment-67b6d9c849-9l988   6m           414Mi           
clip-deployment-67b6d9c849-njv9q   7m           425Mi
```
4. #### `kubectl top node`
```
NAME       CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%   
minikube   163m         8%     1682Mi          43% 
```
