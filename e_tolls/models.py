from django.db import models

# Create your models here.

class TollGate(models.Model):
    gate_id:models.CharField()

class Transaction(models.Model):
    amount_paid:models.IntegerField()
    credits_bought:models.IntegerField()
    tx_id:models.CharField()
    tollGate:models.IntegerField()
    created:models.DateTimeField(auto_now_add=True)
    owner:models.ForeignKey('auth.User',related_name='transactions',on_delete=models.CASCADE)

    class Meta:
        ordering=['created']



