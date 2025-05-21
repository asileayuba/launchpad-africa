from django.shortcuts import render, get_object_or_404
from .models import Sector, Startup, Investor
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    context = {
        'is_landing': True,
    }
    return render(request, "core/home.html", context)

def startup_list_view(request):
    startups = Startup.objects.all().order_by('id')
    paginator = Paginator(startups, 6)
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'startups': startups,
        'page_obj': page_obj,
    }
    return render(request, "core/startups.html", context)

def sector_list_view(request):
    sectors = Sector.objects.all()
    paginator = Paginator(sectors, 6)
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'sectors': sectors,
        'page_obj': page_obj,
    }
    return render(request, "core/sectors.html", context)

def investor(request):
    investors = Investor.objects.all().order_by('id')

    paginator = Paginator(investors, 6)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  

    context = {
        'investors': investors,
        'page_obj': page_obj
    }
    return render(request, "core/investor.html", context)


def about(request):
    return render(request, "core/about.html")

# Search bar / button
def search_startups_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        all_results = Startup.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(sector__name__icontains=query)  # Updated from sectors__name
        ).distinct()

        paginator = Paginator(all_results, 6)  # 6 results per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        results = page_obj
    else:
        page_obj = None

    context = {
        "query": query,
        "results": results,
        "page_obj": page_obj,
    }
    return render(request, 'core/startup_search.html', context)

def startup_detail_view(request, sector_slug, pk):
    startup = get_object_or_404(Startup, pk=pk, sector__slug=sector_slug)  # Updated from sectors__slug
    
    context = {
        'startup': startup,
    }
    return render(request, 'core/startup_detail_by_sector.html', context)

# For list of startups based on their sector
def startups_by_sector_view(request, sector_slug):
    sector = get_object_or_404(Sector, slug=sector_slug)
    startups = Startup.objects.filter(sector=sector)  # Updated from sectors=sector
    paginator = Paginator(startups, 6)
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'sector': sector,
        'startups': startups,
        'page_obj': page_obj,
    }
    return render(request, 'core/startups_by_sector.html', context)



def swagger_ui_view(request):
    return render(request, "swagger_ui.html")