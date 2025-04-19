from .lead.views import LeadViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'leads', LeadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]