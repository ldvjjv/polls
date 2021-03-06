#from django.http import HttpResponse
# Create your views here.
# Writing your first Django app, part 3
#from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import   Http404
from .models import Question



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# Leave the rest of the views (detail, results, vote) unchanged
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
    response = "You're looking at the results of question %s."
def vote(request, question_id):
    return HttpResponse("Estás votando sobre la pregunta %s." % question_id)
