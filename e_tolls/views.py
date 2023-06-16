from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Transaction

# Create your views here.

def verify(request,user_id):
    
    deducted_credits=2
    user =User.objects.get(id=user_id)

    if user is None:
        return HttpResponse(status=404)

    if(user.available_credits<deducted_credits):
        #return error message
        return HttpResponse(status=403)
    
    #Create transaction object
    Transaction.objects.create()
    user.available_credits-=deducted_credits
    user.save()
    return HttpResponse()