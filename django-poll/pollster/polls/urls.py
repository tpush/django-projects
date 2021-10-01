from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='polls-home'),
    path('polls/', views.details, name='polls-detail'),
    path('polls/options/', views.options, name='polls-options'),
    path('<int:question_id>', views.results, name='polls-result')
]
