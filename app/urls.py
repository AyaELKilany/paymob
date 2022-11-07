from .views import createPayment
from django.urls import path

urlpatterns = [
    path('create/' , createPayment)
]
