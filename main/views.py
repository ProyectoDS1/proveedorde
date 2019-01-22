import decimal

from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
from main.models import Subscription


def check_left(request):
    print()
    try:
        phone = request.GET.get("phone")
        value = request.GET.get("value")

        print(f"Received request of {phone} for ${value}")

        subscription = Subscription.objects.get(phone=phone)

        print(f"{phone} has ${subscription.money_left} left")
        if subscription.money_left >= decimal.Decimal(value):
            print("Request accepted!")
            subscription.money_left -= decimal.Decimal(value)
            subscription.save()
            return HttpResponse()

    except Subscription.DoesNotExist:
        pass
    print("Request denied!")
    raise Http404
