from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='property-home'),
    path('results/', views.results, name='property-results'),
]