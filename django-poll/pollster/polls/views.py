from django.views.generic import TemplateView, ListView, DetailView
from .models import Question


class HomeTemplateView(TemplateView):
    template_name = 'polls/home.html'


class QuestionListView(ListView):     # <app><model>_<viewtype>.html
    model = Question
    # context_object_name = 'questions'


class ChoiceDetailView(DetailView):  # <app><model>_<viewtype>.html
    model = Question.objects.filter(question_id)
