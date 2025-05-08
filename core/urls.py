from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("startups/", views.startup_list_view, name="startups"),
    path("sectors/", views.sector_list_view, name="sectors"),
    path("sectors/<slug:sector_slug>/all", views.startups_by_sector_view, name="startups_by_sector"),
    path('sectors/<slug:sector_slug>/<int:pk>/', views.startup_detail_view, name='startup_detail_by_sector'),
    path("investor/", views.investor, name="investor"),
    path("about/", views.about, name="about"),
    path('search/', views.search_startups_view, name='startup_search'),

]
