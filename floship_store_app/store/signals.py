import json

import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from .serializers import OrderSerializer
from .utils import authenticate_user, get_csrf_token, get_user
from .utils import csrf_token


@receiver(post_save, sender=Order)
def create_order_in_warehouse(sender, instance, created, **kwargs):
    if created:
        order = OrderSerializer(instance).data
        json_order = json.dumps(order)
        global csrf_token
        if not csrf_token:
            csrf_token = get_csrf_token()
            user = get_user()
            authenticate_user(user, csrf_token)
        response = requests.post(
            'http://127.0.0.1:8002/api/order/',
            data=json_order,
            cookies={'csrftoken': csrf_token},
            headers={'Content-Type': 'application/json'}
        )
        return response.text
