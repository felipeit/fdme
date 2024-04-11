from django.db import models

from src.findme.infra.orm.user_models import User

class PaymentPlanType(models.Model):
    TYPE_CHOICES = (
        ('free', 1),
        ('trial', 2),
        ('premium', 3)
    )
    type = models.CharField(max_length=200, choices=TYPE_CHOICES, default='free')
    user = models.ForeignKey(User(), on_delete=models.DO_NOTHING)
    free_trial = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)