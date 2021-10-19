# Kubernetes Training/Tutorial

## The problem

Deploy a web application into a node. Consisting of one virtual machine of 8GB RAM, 4 Cores. Usually one would deploy one container. Having more users of the application has the need to scale the application, meaning to create yet another node with the same application running. 

Even worse, say if we have a versioned application, e.g. v2, that we want to deploy. We have to deploy a new node before destroying a prior version, e.g. v1. 

This leaves us with a problem. We would have 12 cores, 24GB RAM, and three containers overall. This is a bit insane. Now, this is where Kubernetes comes into play and can help. 

Kubernetes will take a single node and then utilize the resources in the correct manner. So instead create new nodes, it will fill one node with as many pods as it can (In K8s you can think of pods as a container). This means, instead of having one container per node, we have multiple containers in one node. Kubernetes orchestrates this cluster of us.

![multiple containers](mutliple_containers.png)

**Kubernetes (K8s) is an application orchestrator**

More specifically: 

* K8s deploys and manages containers that run an application (..or else). 
* K8s scales up and down according to demand
* K8s performs zero downtime deployments
* Rollbacks, etc ...

## Components

Let's first have a look at its components.

#### Cluster

A cluster is a set of nodes. A node can be a virtual (VM) or a physical machine, running on the cloud, e.g. Azure, AWS, GCP, or on premise.

#### Nodes

It is important to distinguish between nodes within a K8s cluster. In particular between *master nodes* and *worker nodes*.

The **master node** can be seen as the brain of the cluster. This is where all of the decisions are made. Within the master node, there multiple components that make up the *control plane*, e.g. scheduler, cluster store, API server, cloud controller manager, controller manager.

The **worker nodes** are responsible for the "heavy lifting" of running an application. 

Within one cluster there are often more than one worker node but only one master node.
Master and worker nodes communicate to each other via the *kubelet*.

![kubernetes cluster](kubernetes_cluster.png)

#### Pods

In K8s, a pod is the smallest deployable unit (and not containers). Within a pod there is always one *main container* representing the application (in whatever language written). Further within a pod, there may or may not be *init containers*, and/or *side containers*. Init containers are containers that are executed before the main container. Side containers are containers that support the main containers, e.g. a container that acts as a proxy to your main container. Also within pods there may also be volumes, which enables containers to share data between them. 

Containers communicate with each other within a pod using localhost and whatever port they expose. The port itself has a unique ip adress. This enables communication between pods via the unique adress.

In contrast to K8s, the smallest deployable unit for docker are containers. 


## Commands

To interact with the cluster from our local machine, *kubectl* is needed. 

**kubectl** is a command line tool to run commands against our cluster, e.g. deploy, inspect, edit resources, debug, view logs, etc..
kubectl is also used to connect your cluster, whether it's running in production or any environment.


```bash
# Start a cluster with two nodes
minikube start --nodes=2

# check status of minikube nodes
minikube status

# show docker containers created within nodes
docker ps

# to interact with the cluster use kubectl
# to show available nodes 
kubectl get nodes

# to show all available pods in all namespaces
# this also shows pods of control pane
kubectl get pods -A

# apply configuration file to run.
kubectl apply -f deployment.yml

# to show the cluster-ips and ports
kubectl get svc

# access the running application using the appname
minikube service myapp
```

## Exemplary deployment

To run K8s locally create a local cluster for example using minikube. Make sure do install Docker and Minikube.

To apply the deployment.yml configuration using kubectl use *kubectl apply -f deployment.yml*. *kubectl get pods* should show two pods running now. Check the cluster-ips and ports using *kubectl get svc*. The ports should denote the same as specified within the deployment.yml. Access the running application using the appname
by using *minikube service myapp*. The app can be run within the browser using the shown ip adress.


