from turtle import home
from django.urls import path
from .views import * 

urlpatterns = [
    path('new_question/',newQuestion),
    path('save_question/',saveQuestion),
    path('view_questions/',viewQuestions),
    path('edit_question/',editQuestion),
    path('edit_save_question/',editsaveQuestion),
    path('delete_question/',deleteQuestion), 
    path('signup/',signup),
    path('save_user/',saveUser),
    path('logout/',logout),
    path('login/',login),
    path('login-validation/',loginValidation),
    path('home/',home),
    path('start-test/',startTest),
    path('test-result/',testResult),
   
]
