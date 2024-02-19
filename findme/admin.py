from django.contrib import admin
from findme.models import User, Phone, PaymentPlanType

admin.site.register(User)
admin.site.register(Phone)
admin.site.register(PaymentPlanType)