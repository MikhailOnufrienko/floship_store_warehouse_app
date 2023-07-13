import json

from django.db.models.signals import post_save
from django.dispatch import receiver
import requests

from .models import Order
from .serializers import OrderSerializer


@receiver(post_save, sender=Order)
def create_order_in_warehouse(sender, instance, **kwargs):
    r = requests.get('http://127.0.0.1:8002/admin/')
    cookies = r.cookies
    token = cookies.values()[0]

    response = requests.post(
        'http://127.0.0.1:8002/admin/login/',
        data={'username': 'mikhail', 'password': 'ghast13'},
        cookies={'csrftoken': token},
        headers={'X-CSRFToken': token, 'Content-type': 'application/json'}
    )

    cookies = response.cookies
    token = cookies.values()[0]
  
    order_data = OrderSerializer(instance).data
    json_data = json.dumps(order_data)
    
    response = requests.post(
        'http://127.0.0.1:8002/api/order/',
        data=json_data,
        cookies={'csrftoken': token},
        headers={'Content-Type': 'application/json'}
    )
