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

class Phone(models.Model):
    id = models.UUIDField(primary_key=True)
    phone_number = models.CharField(blank=False, null=False)
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
    type = models.CharField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    free_trial = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)