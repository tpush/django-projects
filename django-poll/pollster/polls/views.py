from django.shortcuts import render
from .models import Question


def home(request):
    return render(request, 'polls/home.html')


def details(request):
    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'polls/details.html', context)


def options(request):
    return render(request, 'polls/options.html')


def results(request):
    return render(request, 'polls/results.html', {'title': 'results'})
