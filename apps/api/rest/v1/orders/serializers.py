# orders/serializers.py
from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from rest_framework.exceptions import PermissionDenied

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ("product", "quantity")

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "user", "status", "items", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at", "user")

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        user = self.context["request"].user

        order = Order.objects.create(user=user, **validated_data)

        for item in items_data:
            product = item["product"]
            quantity = item["quantity"]

            if product.stock < quantity:
                raise serializers.ValidationError(
                    f"Not enough stock for {product.name}. Available: {product.stock}"
                )

            product.stock -= quantity
            product.save()

            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        return order
    
    def update(self, instance, validated_data):
        request = self.context.get("request")
        if "status" in validated_data and not request.user.is_staff:
            raise PermissionDenied("Only admins can change status")
        return super().update(instance, validated_data)

