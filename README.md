# ACEest DevOps – CI/CD Pipeline with Kubernetes

## Overview

This project is a continuation of the ACEest DevOps setup where a complete CI/CD pipeline is implemented and extended up to Kubernetes deployment.

The goal was not just building and testing the app, but actually taking it all the way to deployment using containers and orchestration.

The application used is a simple Flask-based service to simulate a fitness system backend.

---

## What’s Covered in This Assignment

- CI pipeline using Jenkins & GitHub Actions  
- Automated testing using Pytest  
- Docker containerization  
- Docker Hub image push  
- Kubernetes deployment  
- Deployment strategies (Rolling Update + Rollback)  

---

## Tech Stack

- Python (Flask)  
- Git & GitHub  
- Jenkins  
- Pytest  
- Docker  
- Docker Hub  
- Kubernetes  
- SonarQube (Conceptual)  

---

## Project Structure


aceest-devops/
│
├── app.py
├── requirements.txt
├── Dockerfile
│
├── tests/
│ └── test_app.py
│
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
│
└── README.md


---

## CI/CD Workflow


Code Push → GitHub
↓
CI Pipeline Trigger
↓
Run Tests (Pytest)
↓
Build Docker Image
↓
Push to Docker Hub
↓
Deploy to Kubernetes


---

## Running Locally

```bash
python app.py

Runs on:

http://localhost:5000
Running Tests
pytest
Docker Steps
Build Image
docker build -t aceest-app .
Run Container
docker run -p 5000:5000 aceest-app
Kubernetes Deployment

Apply configuration:

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Check resources:

kubectl get pods
kubectl get svc
Deployment Strategy Used
Rolling Update (default Kubernetes strategy)

Rollback command:

kubectl rollout undo deployment aceest-app
Challenges Faced
Jenkins configuration issues
Docker dependency conflicts
Kubernetes networking limitations
NodePort accessibility
Conclusion

This assignment helped in understanding how a real CI/CD pipeline works beyond just testing, especially deployment using Kubernetes.

It demonstrates automation, consistency, and scalability in modern DevOps workflows.