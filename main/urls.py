from django.urls import path
from .views import *

urlpatterns = [
    path('about/', about),
    path('contact/', contact),
    path('', index),
    path('price/', price),
    path('projects/', projects),
    path('services/', services),
    path('sidebarright/', sidebar_right),
    ]
