from rest_framework import generics

from .serializers import OrderSerializer, OrderUpdateSerializer
from .models import Order


class UpdateOrderView(generics.UpdateAPIView):
    serializer_class = OrderUpdateSerializer
    queryset = Order.objects.all()

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)
    