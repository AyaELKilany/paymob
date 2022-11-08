from .views import createPayment , callback , Redirect
from django.urls import path

urlpatterns = [
    path('create/' , createPayment),
    path('callback/' , callback),
    path('redirect/' , Redirect)
]
