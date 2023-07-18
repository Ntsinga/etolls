import datetime
from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase import firebase
from django.http import HttpResponse

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

    #Calculate the timestamp on entry
    timestamp=datetime.datetime.utcnow()
    print(timestamp)
    time=timestamp.time()
    print(time)

    # #Store entry time in the database
    # db.collection("entranceTimestamps").document("bro").set({
    #     "entrytime":timestamp,
    #     "userID":"bro"
    # })

    #return HttpResponse('Ready',content_type='text/plain')

    #Store exit timestamp in database
    # db.collection("exiTimestamps").document("test").set({
    #     "exiTime":timestamp,
    #     "entryTimeID":"",
    #     "user":""
    # })



    #Get entry timestamp
    entry_snapshot=db.collection("entranceTimestamps").document("bro").get()
    entry_data=entry_snapshot.to_dict()
    entry_timestamp=entry_data["entrytime"]
    print(entry_timestamp)
    entry_time=entry_timestamp.time()
    print(entry_time)

    
    #Calculate the difference in time
    time_difference=datetime.datetime.combine(datetime.date.today(),time)-datetime.datetime.combine(datetime.date.today(),entry_time)
    print(time_difference)
    time_difference_str=str(time_difference)
    total_minutes=time_difference.total_seconds()/60
    print(total_minutes)


    #Get the available credits on User's account

    user_snapshot=db.collection("users").document("bro").get()
    user_data=user_snapshot.to_dict()
    available_credits=user_data['credits']
    print(available_credits)
      

    #Calculate the amount of credits to be deducted
    if(total_minutes>30):

        parking_rate=total_minutes/30
        credits=available_credits-parking_rate
        print(credits)
    else:
        credits=credits-2
        print(credits)
        
    #Update user's credit wallet
    db.collection("users").document("bro").update({
            "credits":credits
        })

    #Create credit_transaction receipt

    db.collection("transactions").document("bro").set({
    "Parking Time":time_difference_str,
    "amount":parking_rate,
    "balance":credits,
    "date":timestamp,
    "type":"credit",
    "user":"bro"
    })


    return HttpResponse('Success',content_type='text/plain')


  



