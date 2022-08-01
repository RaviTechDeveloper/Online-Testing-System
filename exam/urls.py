from django.urls import path
from .views import *

urlpatterns = [
    path('test-paper/',testPaper),
    path('test-result/',testResult),
   
]
