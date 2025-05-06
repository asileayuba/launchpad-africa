from django.shortcuts import render
from rest_framework import viewsets
from core.models import Startup
from .serializers import StartupSerializer



class StartupViewSet(viewsets.ModelViewSet):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
