from django.shortcuts import render, get_object_or_404
from .models import Sector, Startup
from django.db.models import Q


def home(request):
    context={
        'is_landing': True,
    }
    return render(request, "core/home.html", context)

def startup_list_view(request):
    startups = Startup.objects.all()
    
    context = {
        'startups': startups,
    }
    return render(request, "core/startups.html", context)


def sector_list_view(request):
    sectors = Sector.objects.all()
    
    context = {
        'sectors': sectors,
    }
    return render(request, "core/sectors.html", context)

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

# Search bar / button
def search_startups_view(request):
    query = request.GET.get('q')
    results = []
    
    if query:
        results = Startup.objects.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) | 
            Q(sectors__name__icontains=query))
        
    context = {
        "query": query,
        "results": results,
    }
    return render(request, 'core/startup_search.html', context)

def startup_detail_view(request, sector_slug, pk):
    startup = get_object_or_404(Startup, pk=pk, sectors__slug=sector_slug)
    
    context = {
        'startup': startup,
    }
    return render(request, 'core/startup_detail_by_sector.html', context)

# For list of startups based on their sector
def startups_by_sector_view(request, sector_slug):
    sector = get_object_or_404(Sector, slug=sector_slug)
    startups = Startup.objects.filter(sectors=sector)
    
    context = {
        'sector': sector,
        'startups': startups
    }
    return render(request, 'core/startups_by_sector.html', context)
