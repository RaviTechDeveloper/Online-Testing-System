from django.urls import path
from .views import *


urlpatterns = [
   
    path('Hello',greeting),
    path('about/',about),
    path('contacts/',contacts),
   
]
