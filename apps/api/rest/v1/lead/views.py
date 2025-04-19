from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.lead.models import Lead
from .serializers import LeadSerializer, LeadCreateSerializer, LeadUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedOrCreateOnly
from .email_utils import send_lead_confirmation_email, send_attorney_notification_email

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [IsAuthenticatedOrCreateOnly]
    
    def get_serializer_class(self):
        if self.action == 'create' and not self.request.user.is_authenticated:
            return LeadCreateSerializer
        elif self.action == 'update_status':
            return LeadUpdateSerializer
        return LeadSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        lead = serializer.save()
        
        send_lead_confirmation_email(lead)
        send_attorney_notification_email(lead)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    def update_status(self, request, pk=None):
        lead = self.get_object()
        serializer = LeadStatusUpdateSerializer(lead, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'update', 'partial_update', 'destroy', 'update_status']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()