from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('confirm/<uuid:token>/', views.confirm_subscription, name='confirm_subscription'),
    path('unsubscribe/<uuid:token>/', views.unsubscribe, name='unsubscribe'),
]