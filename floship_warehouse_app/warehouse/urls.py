from django.urls import path

from .views import CreateOrderView


urlpatterns = [
    path('order/', CreateOrderView.as_view()),
]
