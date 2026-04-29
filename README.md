ACEest DevOps – CI/CD Pipeline with Kubernetes

Overview

This project is a continuation of the ACEest DevOps setup where a complete CI/CD pipeline is implemented and extended up to Kubernetes deployment.

The goal here was not just building and testing the app, but actually taking it all the way to deployment using containers and orchestration.

The application used is a simple Flask-based service to simulate a fitness system backend.

What’s Covered in This Assignment
CI pipeline using Jenkins & GitHub Actions
Automated testing using Pytest
Docker containerization
Docker Hub image push
Kubernetes deployment
Deployment strategies (Rolling update + Rollback)
Tech Stack
Python (Flask)
GitHub
Jenkins
Pytest
Docker
Docker Hub
Kubernetes
SonarQube (studied)
Project Structure
aceest-devops/
│
├── app.py
├── requirements.txt
├── Dockerfile
│
├── tests/
│   └── test_app.py
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
└── README.md
How It Works (Flow)
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
Running Locally
python app.py

Runs on:

http://localhost:5000
Running Tests
pytest
Docker Steps

Build image:

docker build -t aceest-app .

Run container:

docker run -p 5000:5000 aceest-app
Kubernetes Deployment

Apply configs:

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

Check:

kubectl get pods
kubectl get svc
Deployment Strategy Used
Rolling Update (default Kubernetes)
Rollback tested using:
kubectl rollout undo deployment aceest-app
Challenges Faced
Jenkins setup issues
Docker build errors
Kubernetes networking
NodePort access problem
Conclusion

This assignment helped in understanding how real CI/CD pipelines work beyond just testing — especially deployment using Kubernetes.
