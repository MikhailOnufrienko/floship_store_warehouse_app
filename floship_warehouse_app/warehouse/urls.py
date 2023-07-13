from django.urls import path
from rest_framework import routers

from warehouse.views import CreateOrderView


urlpatterns = [
    path('order/', CreateOrderView.as_view()),
]

