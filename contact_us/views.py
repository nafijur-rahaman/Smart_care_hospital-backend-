from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactUs
from .serializers import ContactUsSerializer
# Create your views here.

class ContactusViews(viewsets.ModelViewSet):
    queryset=ContactUs.objects.all()
    serializer_class=ContactUsSerializer
    