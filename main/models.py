from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Subscription(models.Model):
    ACTIVE = 1
    INACTIVE = 0
    STATUS_CHOICES = (
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive")
    )

    username = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS_CHOICES, default=ACTIVE)
    money_left = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.username}: ${self.money_left}"
