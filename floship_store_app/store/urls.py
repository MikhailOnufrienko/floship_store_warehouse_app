from django.urls import path

from store.views import UpdateOrderView


urlpatterns = [
    path('order/<int:pk>/', UpdateOrderView.as_view()),
]
