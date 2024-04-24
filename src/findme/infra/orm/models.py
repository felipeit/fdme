from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    active = models.BooleanField(default=False)
    age = models.IntegerField(null=True)


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