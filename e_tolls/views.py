from django.shortcuts import render





# firebase= pyrebase.initialize_app(config)
# authe=firebase.auth()
# database=firebase.database()

def verify(request):
    # userID= database.child('User Data').child('userID').get().val()
    #     stack = database.child('Data').child('Stack').get().val()
    #     framework = database.child('Data').child('Framework').get().val()
    
    # deducted_credits=2
    # user =User.objects.get(id=user_id)

    # if userID is None:
    return render(request,"index.html")

    # if(user.available_credits<deducted_credits):
    #     #return error message
    #     return HttpResponse(status=403)
    
    # #Create transaction object
    # Transaction.objects.create()
    # user.available_credits-=deducted_credits
    # user.save()
    # return HttpResponse()



