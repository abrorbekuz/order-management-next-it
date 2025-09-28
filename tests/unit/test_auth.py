import pytest

@pytest.mark.django_db
def test_register_user(api_client):
    data = {"username": "newuser", "email": "new@example.com", "password": "StrongPass123!"}
    response = api_client.post("/api/v1/auth/register/", data, format="json")
    assert response.status_code == 201
    assert "access" in response.data
    assert "refresh" in response.data
    assert response.data["user"]["username"] == "newuser"

@pytest.mark.django_db
def test_register_duplicate_username(api_client, user):
    
    data = {"username": user.username, "email": "other@example.com", "password": "StrongPass123!"}
    response = api_client.post("/api/v1/auth/register/", data, format="json")
    assert response.status_code == 400
    assert "username" in str(response.data)

@pytest.mark.django_db
def test_login_user(api_client, user):
    data = {"username": user.username, "password": "pass123"}
    response = api_client.post("/api/v1/auth/token/", data, format="json")
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_login_wrong_password(api_client, user):
    data = {"username": user.username, "password": "wrongpass"}
    response = api_client.post("/api/v1/auth/token/", data, format="json")
    assert response.status_code == 401
