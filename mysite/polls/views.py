
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_questions_list = Question.objects.order_by('-pub_date')[:5]
    tempplate = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_questions_list,
    }

    return HttpResponse(tempplate.render(context, request))


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    return HttpResponse(f"You are looking at the results of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
