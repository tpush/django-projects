from django.views.generic import TemplateView, ListView, DetailView
from .models import Question, Choice
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# from django.views import View


class HomeTemplateView(TemplateView):
    template_name = 'polls/home.html'


class QuestionListView(ListView):     # <app><model>_<viewtype>.html
    model = Question
    # context_object_name = 'questions'


class ChoiceDetailView(DetailView):  # <app><model>_<viewtype>.html
    model = Question


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/question_list.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls-result', args=(question.id,)))
