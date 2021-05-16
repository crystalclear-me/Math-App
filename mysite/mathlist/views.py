from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'mathlist/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return a list of Questions Level
        """
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = 'mathlist/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'mathlist/results.html'


def selection(request, question_id):
    template_select_for = loader.get_template('mathlist/detail.html')
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
        'error_message': "You didn't select a choice.",
    }
    #update all selection to zero prior user select so the program will know which one is being selected
    p = Choice.objects.all().update(selection=0)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question select form.
        return HttpResponse(template_select_for.render(context, request))
    else:
        selected_choice.selection = 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('mathlist:results', args=(question.id,)))
