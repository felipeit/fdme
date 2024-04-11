from django.db import models


class User(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    cpf = models.CharField(max_length=11)
    cnpj = models.CharField(max_length=14)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    active = models.BooleanField(default=True)
    age = models.IntegerField()
