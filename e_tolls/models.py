from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=50,unique=True)
    email=models.CharField(max_length=100,unique=True)
    phone=models.CharField(max_length=15)
    available_credits=models.IntegerField()


class Transaction(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    amount_paid=models.CharField(max_length=10,default='2 credits')

  #Attaching transaction object to a user
    user=models.ForeignKey(User,related_name='transactions',on_delete=models.CASCADE)

    class Meta:
        ordering=['created']



