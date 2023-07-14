from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase

cred=credentials.Certificate('e_tolls/serviceAccountKey.json')
default_app=firebase_admin.initialize_app(cred)
db=firestore.client()
firebase=firebase.FirebaseApplication("https://etolls-8d93b-default-rtdb.firebaseio.com",None)

def verify(request):

    
    # doc = db.collection('users').document('yMtsidNmTFUsk3CyS3rtGOruo8v1').get()
    # s=doc.to_dict()
    # print(s)

    # db.collection("users").document("yMtsidNmTFUsk3CyS3rtGOruo8v1").set({
    #     "email":"benj1234@gmail.com",
    #     "name":"Ssempala"
    # })
    # db.collection("users").document("bro").set({
    #     "email":"benj1234@gmail.com",
    #     "name":"Ssempala"
    # })

    return render(request,"index.html",status=404)
  
    # deducted_credits=2
    # user =User.objects.get(id=user_id)

    # if userID is None:
    

    # if(user.available_credits<deducted_credits):
    #     #return error message
    #     return HttpResponse(status=403)
    
    # #Create transaction object
    # Transaction.objects.create()
    # user.available_credits-=deducted_credits
    # user.save()
    # return HttpResponse()



