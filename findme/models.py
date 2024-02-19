# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    id = models.UUIDField()
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.EmailField()
    cpf = models.CharField()
    cnpj = models.CharField()
    address = models.CharField()
    phone_number = models.CharField()
    active = models.BooleanField(default=True)


class Phone(models.Model):
    id = models.UUIDField()
    phone_number = models.CharField()
    imei = models.CharField()
    model = models.CharField()
    os = models.CharField()
    user = models.ForeignKey(User)
    latitude = models.CharField()
    longitude = models.CharField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class PaymentPlanType(models.Model):
    type = models.CharField()
    user = models.ForeignKey(User)
    free_trial = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)