from e_tolls.models import Transaction
from rest_framework import serializers
from django.contrib.auth.models import User


class TransactionSerializer(serializers.Serializer):
    amount_paid=serializers.IntegerField()
    credits_bought=serializers.IntegerField()
    tx_id=serializers.CharField()
    tollGate=serializers.IntegerField()


    def create(self,validated_data):
        return Transaction.objects.create(**validated_data)
    
class TollGateSerializer(serializers.Serializer):
    gate_id=serializers.IntegerField()

class UserSerializer(serializers.ModelSerializer):
    transactions=serializers.PrimaryKeyRelatedField(many=True,queryset=Transaction.objects.all())
    
    class Meta:
        model=User
        fields=['id','username','password']

    
