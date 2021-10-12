from django.urls import path
from .views import HomeTemplateView, QuestionListView, ChoiceDetailView, ResultDetailView
from . import views

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='polls-home'),
    path('polls/', QuestionListView.as_view(), name='polls-detail'),
    path('polls/<int:pk>/', ChoiceDetailView.as_view(), name='polls-option'),
    path('polls/<int:pk>/results', ResultDetailView.as_view(), name='polls-result'),
    path('polls/<int:question_id>/votes', views.vote, name='polls-vote'),
]
