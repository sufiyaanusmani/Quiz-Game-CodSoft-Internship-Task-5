from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home-page'),
    path('quiz/', views.quizPage, name='quiz-page'),
    # path('result/', views.resultPage, name='result-page'),
]