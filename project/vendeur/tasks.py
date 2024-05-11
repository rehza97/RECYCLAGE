# tasks.py

from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from .models import AllCommandes

@shared_task
def update_alert():
    threshold_date = timezone.now() - timedelta(days=7)
    AllCommandes.objects.filter(created_date__lt=threshold_date, alert=False).update(alert=True)
