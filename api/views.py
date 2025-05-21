from django.shortcuts import render
from rest_framework import viewsets, filters
from core.models import Startup
from .serializers import StartupSerializer
from rest_framework_api_key.permissions import HasAPIKey
from .permissions import HasAPIKeyWithCount


class StartupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    permission_classes = [HasAPIKeyWithCount]  
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'location', 'sector__name']
    ordering_fields = ['id']