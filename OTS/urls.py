from django.urls import path
from .views import *

urlpatterns = [
    path('new_question/',newQuestion),
    path('save_question/',saveQuestion),
    path('view_questions/',viewQuestions),
   
   
]
