from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer


class UpdateOrderView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_serializer(self, *args, **kwargs):
        kwargs['partial'] = True
        return super().get_serializer(*args, **kwargs)
