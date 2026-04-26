import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


def test_home():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200


def test_health():
    tester = app.test_client()
    response = tester.get("/health")
    assert response.status_code == 200

def test_members():
    client = app.test_client()
    response = client.get('/members')
    assert response.status_code == 200

def test_invalid_route():
    client = app.test_client()
    response = client.get('/invalid')
    assert response.status_code == 404

def test_status_content():
    client = app.test_client()
    response = client.get('/')
    assert b"ACEest Fitness DevOps Application Running" in response.data