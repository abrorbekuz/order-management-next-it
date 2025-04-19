from django.conf import settings
from django.core.mail import send_mail
from .utils import run_silent

@run_silent
def send_lead_confirmation_email(lead):
    subject = 'Thank you for your interest'
    message = f"""
    Dear {lead.first_name} {lead.last_name},
    
    Thank you for submitting your information. Our team will review your resume and reach out to you shortly.
    
    Best regards,
    The Legal Team
    """
    
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[lead.email],
        fail_silently=False,
    )

@run_silent
def send_attorney_notification_email(lead):
    subject = f'New Lead Submitted: {lead.first_name} {lead.last_name}'
    message = f"""
    A new lead has been submitted:
    
    Name: {lead.first_name} {lead.last_name}
    Email: {lead.email}
    Submitted on: {lead.created_at}
    
    Please login to the system to view the resume and manage this lead.
    """
    
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ATTORNEY_EMAIL],
        fail_silently=False,
    )