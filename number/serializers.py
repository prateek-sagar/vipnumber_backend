from rest_framework import serializers
from .models import *

class NumberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'

