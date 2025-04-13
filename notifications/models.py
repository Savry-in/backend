from django.db import models
from django.conf import settings
from inventory.models import Inventory

class Notification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ('app', 'In-App'),
        ('email', 'Email'),
    ]
    NOTIFICATION_STATUS_CHOICES = [
        ('sent', 'Sent'),
        ('scheduled', 'Scheduled'),
        ('failed', 'Failed'),
    ]

    notification_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=True, blank=True)
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPE_CHOICES, default='app')
    message = models.TextField()
    status = models.CharField(max_length=10, choices=NOTIFICATION_STATUS_CHOICES, default='scheduled')
    sent_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = 'notification'

    def __str__(self):
        return f"{self.notification_type} - {self.status}"
