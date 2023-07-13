from django.urls import path

from store.views import UpdateOrderView


urlpatterns = [
    path('order/<int:pk>/update/', UpdateOrderView.as_view()),
]
