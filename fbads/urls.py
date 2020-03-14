from django.urls import path
from . import views


urlpatterns = [
    path('', views.fbads, name='dashboard.html'),
    path('fb-ads', views.all_ads, name='all-ads.html'),
]