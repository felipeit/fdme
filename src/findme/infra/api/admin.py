from django.contrib import admin
from src.findme.infra.orm.models import User
from src.findme.infra.orm.models import Phone
from src.findme.infra.orm.models import PaymentPlanType


admin.site.register(User)
admin.site.register(Phone)
admin.site.register(PaymentPlanType)