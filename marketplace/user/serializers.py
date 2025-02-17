from rest_framework import serializers
from .models import customer

class CustomerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['id', 'name', 'email', 'gender','username','password']  # Fields to include in API



