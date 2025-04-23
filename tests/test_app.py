import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app
import pytest

def test_example():
    assert 1 + 1 == 2, "Basic math test failed"

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200, f"Home page returned {response.status_code} instead of 200"
    assert b"Welcome" in response.data, "Response data: " + str(response.data)

def test_dashboard_requires_login():
    client = app.test_client()
    response = client.get('/dashboard')
    assert response.status_code == 302, f"Dashboard returned {response.status_code} instead of redirect (302)"
    assert '/login' in response.location, f"Expected redirect to login, got {response.location}"

def test_invalid_route_returns_404():
    client = app.test_client()
    response = client.get('/nonexistent')
    assert response.status_code == 404, f"Invalid route returned {response.status_code} instead of 404"