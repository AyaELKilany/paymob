from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny
from .models import Payment
from rest_framework.response import Response
import requests



@api_view(['POST'])
@permission_classes([AllowAny])
def createPayment(request):
    data = request.data

    payload = {
    "api_key" : "ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnVZVzFsSWpvaU1UVTFNelU0T0RVMU5pNHdNemcxTmpJaUxDSndjbTltYVd4bFgzQnJJam96TURZeExDSmpiR0Z6Y3lJNklrMWxjbU5vWVc1MEluMC5hQUVSSVVjdVZlVl9kb3ZnZ3FfZFB4T3JSUm80UjJLdUNlRlNiMDMzMzd3WDg1WnBJb3VxMS11TXV4UjJVVngxWldYQlQ1cnhoZ1IxTVlLNW9QNHJrdw=="
    }
    
    res = requests.post("https://accept.paymob.com/api/auth/tokens" , json=payload)
    final_response = res.json()
    token = final_response['token']
    
    payload = {
        'auth_token' : token,
        'delivery_needed' : False,
        'amount_cents' : data['value'],
        'items' : [],
    }
    
    res = requests.post("https://accept.paymob.com/api/ecommerce/orders" , json=payload)
    final_response = res.json()
    order_id = final_response['id']
    
    payment = Payment(
        client_name=data['client_name'],
        value=data['value'],
        currency=data['currency'],
        order_id=order_id
    )
    payment.save()
    
    payload ={
        'auth_token' : token,
        'amount_cents' : data['value'],
        'expiration' : 3600,
        'order_id' : order_id,
        'billing_data' : {
            'first_name' : data['client_name'],
            "apartment": "803", 
            "email": "claudette09@exa.com", 
            "floor": "42",
            "street": "Ethan Land", 
            "building": "8028", 
            "phone_number": "+86(8)9135210487", 
            "shipping_method": "PKG", 
            "postal_code": "01898", 
            "city": "Jaskolskiburgh", 
            "country": "CR", 
            "last_name": "Nicolas", 
            "state": "Utah"
        },
        'currency' : data['currency'],
        'integration_id' : '4658'
    }
    
    res = requests.post("https://accept.paymob.com/api/acceptance/payment_keys" , json=payload)
    final_response = res.json()
    payment_token = final_response['token']
    
    payload = {
        "payment_token" : payment_token
    }
    res = requests.post("https://accept.paymob.com/api/acceptance/iframes/29754?" , params=payload)
    print(res.url)
    # return HttpResponseRedirect(reverse("http://pay.teqneia.com/api/invoice"))
    return Response({'message': 'Frame Created Successfully' + res.url})


@api_view(['GET'])
@permission_classes([AllowAny])
def callback(request):
    transaction_status = request.GET.get('success')
    order = request.GET.get('order')
    if transaction_status == 'true':
        payment = Payment.objects.get(order_id = order)
        print(payment.status)
        payment.status = True
        print(payment.status)
        return Response({'message' : 'Your transaction is done.'})
    else:
        return Response({'Error message:' : 'There was a problem with the transaction'})

    
    