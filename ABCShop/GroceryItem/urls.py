

from django.urls import path
from GroceryItem import views

urlpatterns = [
    path('makeEntry/', views.makeEntry),
    path('dispEntry/', views.dispEntries),
    
    ]
