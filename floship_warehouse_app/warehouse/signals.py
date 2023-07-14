import json
import logging

import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from .serializers import OrderSerializer
from project_config import project_settings
from shared_utils.utils import authenticate_user, get_csrf_token, get_user
from shared_utils.utils import csrf_token


APP_NAME = project_settings.WAREHOUSE_APP_NAME

OTHER_APP_NAME = project_settings.STORE_APP_NAME

OTHER_APP_PORT = project_settings.STORE_APP_PORT

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Order)
def update_order_in_store(sender, instance, created, **kwargs):
    """A signal updating an order in the store app."""

    if not created:
        order = OrderSerializer(instance).data
        order_id = order.get('id')
        json_order = json.dumps(order)
        global csrf_token
        if not csrf_token:
            csrf_token = get_csrf_token(OTHER_APP_PORT)
            user = get_user(APP_NAME)
            authenticate_user(user, csrf_token, OTHER_APP_PORT)
        response = requests.patch(
            f'http://127.0.0.1:{OTHER_APP_PORT}/api/order/{order_id}/update/',
            data=json_order,
            cookies={'csrftoken': csrf_token},
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 200:
            logger.info(f'Заказ {order_id} обновлён '
                        f'в приложении {OTHER_APP_NAME}.')
        if response.status_code == 404:
            logger.info(f'Заказа {order_id} в приложении '
                        f'{OTHER_APP_NAME} не существует.')
