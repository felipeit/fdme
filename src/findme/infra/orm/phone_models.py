from django.db import models
from src.findme.infra.orm.user_models import User

class Phone(models.Model):
    id = models.UUIDField(primary_key=True)
    phone_number = models.CharField(max_length=11, blank=False, null=False)
    imei = models.CharField(max_length=15, blank=False, null=False)
    model = models.CharField(max_length=200, blank=True, null=True)
    os = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    active = models.BooleanField(default=True)
