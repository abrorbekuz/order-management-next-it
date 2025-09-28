from rest_framework import viewsets
from apps.products.models import Product
from .serializers import ProductSerializer
from .permissions import IsAdmin

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]
