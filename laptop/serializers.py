from rest_framework import serializers
from .models import *

class LaptopAllSerializers(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields =("name", "color", "user")
