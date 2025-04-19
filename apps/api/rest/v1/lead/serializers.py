from rest_framework import serializers
from apps.lead.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'first_name', 'last_name', 'email', 'resume', 'status', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class LeadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'email', 'resume']


class LeadUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['status']