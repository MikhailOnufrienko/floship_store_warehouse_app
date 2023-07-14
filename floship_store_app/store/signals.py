import json

import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from .serializers import OrderSerializer
from shared_utils.utils import authenticate_user, get_csrf_token, get_user
from shared_utils.utils import csrf_token
from project_config import project_settings


APP_NAME = project_settings.STORE_APP_NAME

OTHER_APP_PORT = project_settings.WAREHOUSE_APP_PORT


@receiver(post_save, sender=Order)
def create_order_in_warehouse(sender, instance, created, **kwargs):
    if created:
        order = OrderSerializer(instance).data
        json_order = json.dumps(order)
        global csrf_token
        if not csrf_token:
            csrf_token = get_csrf_token(OTHER_APP_PORT)
            user = get_user(APP_NAME)
            authenticate_user(user, csrf_token, OTHER_APP_PORT)
        response = requests.post(
            f'http://127.0.0.1:{OTHER_APP_PORT}/api/order/',
            data=json_order,
            cookies={'csrftoken': csrf_token},
            headers={'Content-Type': 'application/json'}
        )
        return response.text
