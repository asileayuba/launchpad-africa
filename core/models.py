from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from rest_framework_api_key.models import APIKey


# Sector Model
class Sector(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    logo = CloudinaryField('logo', null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    
# Startup Model 
class Startup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    founding_date = models.DateField()
    logo = CloudinaryField('logo', null=True, blank=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    website = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    
    def __str__(self):
        return self.name

# Investors Model
class Investor(models.Model):
    name = models.CharField(max_length=255)
    logo = CloudinaryField('logo', null=True, blank=True)
    email = models.EmailField(unique=True)
    investment_type = models.CharField(max_length=100)
    country = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class APIKeyMeta(models.Model):
    api_key = models.OneToOneField(APIKey, on_delete=models.CASCADE, related_name='meta')
    email = models.EmailField()
    request_count = models.PositiveIntegerField(default=0)
    revoked = models.BooleanField(default=False)  # Optional, mirror APIKey revocation if needed

    def __str__(self):
        return f"{self.email} - {self.api_key.name}"