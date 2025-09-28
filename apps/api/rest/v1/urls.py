from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .auth.views import RegisterView
from rest_framework.permissions import AllowAny

from .products.views import ProductViewSet
from .orders.views import OrderViewSet


router = DefaultRouter()

router.register(r"products", ProductViewSet, basename="product")
router.register(r"orders", OrderViewSet, basename="order")

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path('auth/token/', TokenObtainPairView.as_view(
        permission_classes=[AllowAny]), name='token_obtain_pair'),
    path('auth/token/refresh/',
         TokenRefreshView.as_view(permission_classes=[AllowAny]), name='token_refresh'),
         
    path('', include(router.urls)),
]