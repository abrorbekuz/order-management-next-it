import pytest

@pytest.mark.django_db
def test_product_list(api_client, user, admin, products):
    api_client.force_authenticate(user=user)
    response = api_client.get("/api/v1/products/")
    assert response.status_code in [403, 401]


    api_client.force_authenticate(user=admin)
    response = api_client.get("/api/v1/products/")

    assert response.status_code == 200
    assert len(response.data['results']) == len(products)

@pytest.mark.django_db
def test_product_detail(api_client, admin, products):
    product = products[0]
    api_client.force_authenticate(user=admin)

    response = api_client.get(f"/api/v1/products/{product.id}/")
    assert response.status_code == 200
    assert response.data['id'] == product.id
    assert response.data['name'] == product.name

@pytest.mark.django_db
def test_product_create_permission(api_client, user):
    data = {"name": "SecretProduct", "price": 10, "stock": 5}
    
    api_client.force_authenticate(user=user)
    response = api_client.post("/api/v1/products/", data, format="json")
    assert response.status_code in [403, 401]

@pytest.mark.django_db
def test_product_create_admin(api_client, admin):
    data = {"name": "AdminProduct", "price": 15, "stock": 10}
    api_client.force_authenticate(user=admin)
    response = api_client.post("/api/v1/products/", data, format="json")
    assert response.status_code == 201
    assert response.data["name"] == "AdminProduct"
