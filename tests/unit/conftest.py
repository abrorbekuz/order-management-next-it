import pytest

from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.products.models import Product


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username="user1", email="usersan@gmail.com", password="pass123")

@pytest.fixture
def admin():
    return User.objects.create_superuser(username="admin", email="usersan@gmail.com", password="admin123")

@pytest.fixture
def products():
    p1 = Product.objects.create(name="Product 1", price=10.0, stock=5)
    p2 = Product.objects.create(name="Product 2", price=20.0, stock=2)
    return [p1, p2]