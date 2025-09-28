from apps.orders.models import Order, OrderItem
from django.contrib.auth.models import User
import pytest

@pytest.mark.django_db
def test_order_creation_not_enough_stock(api_client, user, products):
    api_client.force_authenticate(user=user)
    data = {
        "items": [{"product": products[1].id, "quantity": 10}]
    }
    response = api_client.post("/api/v1/orders/", data, format="json")
    assert response.status_code == 400
    assert "Not enough stock" in str(response.data)

@pytest.mark.django_db
def test_order_view_permissions(api_client, user, admin, products):
    
    order = Order.objects.create(user=user)
    OrderItem.objects.create(order=order, product=products[0], quantity=1)

    
    api_client.force_authenticate(user=user)
    response = api_client.get("/api/v1/orders/")
    assert response.status_code == 200
    assert len(response.data['results']) == 1

    other_user = User.objects.create_user(username="user2")
    api_client.force_authenticate(user=other_user)
    response = api_client.get("/api/v1/orders/")
    assert len(response.data['results']) == 0

    api_client.force_authenticate(user=admin)
    response = api_client.get("/api/v1/orders/")
    assert len(response.data['results']) == 1


@pytest.mark.django_db
def test_order_status_change_permission(api_client, user, admin, products):
    order = Order.objects.create(user=user)
    
    
    api_client.force_authenticate(user=user)
    response = api_client.patch(f"/api/v1/orders/{order.id}/", {"status": "completed"}, format="json")
    assert response.status_code == 403

    
    api_client.force_authenticate(user=admin)
    response = api_client.patch(f"/api/v1/orders/{order.id}/", {"status": "completed"}, format="json")
    assert response.status_code == 200
    order.refresh_from_db()
    assert order.status == "completed"
