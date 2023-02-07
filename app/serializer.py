from app.models import student
from rest_framework import serializers
class Studentserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=student
        fields='__all__'