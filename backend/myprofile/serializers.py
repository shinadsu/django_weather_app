from .models import Myprofile
from rest_framework import serializers


class MyProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Myprofile
        fields = ('__all__')
