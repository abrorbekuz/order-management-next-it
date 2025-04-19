from django.contrib import admin
from apps.lead.models import Lead

class LeadAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ['-created_at']
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'resume', 'status')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Lead, LeadAdmin)
