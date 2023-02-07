from django.shortcuts import render
from app.models import student
from app.serializer import Studentserializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class studentcrud(ModelViewSet):
    queryset=student.objects.all()
    serializer_class=Studentserializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]
