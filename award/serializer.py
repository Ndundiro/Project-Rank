from rest_framework import serializers
from .models import Project


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        models = Project
        fields = ('sitename','description','url','screenshot','user','submit','overall')


    