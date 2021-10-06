from django.urls import path
from .views import QuestionListView, ChoiceDetailView
from . import views

urlpatterns = [
    path('', views.home, name='polls-home'),
    path('polls/', QuestionListView.as_view(), name='polls-detail'),
    path('polls/<int:pk>/', ChoiceDetailView.as_view(), name='polls-option')
]
