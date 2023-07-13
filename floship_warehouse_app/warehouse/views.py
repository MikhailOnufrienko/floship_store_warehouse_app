from rest_framework import generics

from .serializers import OrderSerializer
from .models import Order


class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()