from django.contrib import admin
from src.findme.infra.orm.user_models import User
from src.findme.infra.orm.phone_models import Phone
from src.findme.infra.orm.paymentplantype_models import PaymentPlanType


admin.site.register(User)
admin.site.register(Phone)
admin.site.register(PaymentPlanType)