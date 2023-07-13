import json

import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from .serializers import OrderSerializer
from .utils import authenticate_user, get_csrf_token, get_user
from .utils import csrf_token


@receiver(post_save, sender=Order)
def update_order_in_store(sender, instance, created, **kwargs):
    if not created:
        order = OrderSerializer(instance).data
        order_id = order.get('id')
        json_order = json.dumps(order)
        global csrf_token
        if not csrf_token:
            csrf_token = get_csrf_token()
            user = get_user()
            authenticate_user(user, csrf_token)
        response = requests.patch(
            f'http://127.0.0.1:8001/api/order/{order_id}/update/',
            data=json_order,
            cookies={'csrftoken': csrf_token},
            headers={'Content-Type': 'application/json'}
        )
        return response.text
