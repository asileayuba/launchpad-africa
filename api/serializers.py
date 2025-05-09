from rest_framework import serializers
from core.models import Startup

class StartupSerializer(serializers.ModelSerializer):
    sector = serializers.CharField(source='sector.name')
    
    class Meta:
        model = Startup
        fields = ['id', 'name', 'description', 'founding_date', 'website', 'location', 'sector']