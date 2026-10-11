# Iris ML Prediction API on Kubernetes

A Flask API serving a RandomForest Iris classifier, containerized with Docker and deployed on a local Kubernetes cluster (minikube) with 2 replicas.

## Tech Stack
Python, Flask, scikit-learn, Docker, Kubernetes (minikube), kubectl

## Project Structure
- `app.py` : Flask API with `/` and `/predict` endpoints
- `Dockerfile` : container image definition
- `deployment.yaml` : Kubernetes Deployment (2 replicas)
- `service.yaml` : Kubernetes Service

## How to Run

```bash
docker build -t iris-api:v1 .
minikube start --driver=docker
minikube image load iris-api:v1
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl port-forward svc/iris-service 8080:80
```

## Test the API

```powershell
Invoke-RestMethod -Uri http://localhost:8080/predict -Method Post -ContentType "application/json" -Body '{"features":[5.1,3.5,1.4,0.2]}'
```

## Output

**Pods running on Kubernetes (2 replicas):**

```
NAME                        READY   STATUS    RESTARTS   AGE
iris-api-6b6889d94c-59lkf   1/1     Running   0          2m3s
iris-api-6b6889d94c-vb54x   1/1     Running   0          2m3s
```

**API home endpoint:**

```json
{"message":"Iris ML API running","pod":"iris-api-6b6889d94c-59lkf"}
```

**Prediction endpoint:**

```
pod                       prediction
---                       ----------
iris-api-6b6889d94c-59lkf setosa
```