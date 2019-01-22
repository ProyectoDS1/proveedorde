import decimal

from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.
from main.models import Subscription


def check_left(request):
    try:
        subscription = Subscription.objects.get(phone=request.GET.get("phone"))
        if subscription.money_left >= decimal.Decimal(request.GET.get("value")):
            subscription.money_left -= decimal.Decimal(request.GET.get("value"))
            subscription.save()
            return HttpResponse()
        raise Http404
    except Subscription.DoesNotExist:
        raise Http404
