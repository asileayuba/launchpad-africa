from django.db import models
from django.utils.text import slugify



class Sector(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to='sector_logos/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug =slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    

class Startup(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    founding_date = models.DateField()
    logo = models.ImageField(upload_to='logos/')
    sectors = models.ForeignKey(Sector, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
