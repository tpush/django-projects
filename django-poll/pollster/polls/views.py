from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Question, Choice


def home(request):
    return render(request, 'polls/home.html')


class QuestionListView(ListView):
    model = Question
    template_name = 'polls/details.html'
    context_object_name = 'questions'


class ChoiceDetailView(DetailView):  # <app><model>_<viewtype>.html
    model = Choice


def results(request):
    return render(request, 'polls/results.html', {'title': 'results'})
