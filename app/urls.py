from .views import createPayment , callback
from django.urls import path

urlpatterns = [
    path('create/' , createPayment),
    path('callback' , callback)
]
