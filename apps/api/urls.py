from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('v1/', include('apps.api.rest.v1.urls')),
    path('auth/', include('rest_framework.urls')),
]