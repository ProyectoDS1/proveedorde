from django.contrib import admin

# Register your models here.
from main.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass
