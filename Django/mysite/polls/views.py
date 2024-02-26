from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Question
from .Catalogo import Catalogo
import pandas as pd
from IPython.display import HTML

def index(request):
    data_list = Catalogo().read()
    Df = []
    for row in data_list:
        Df.append(row.to_dict())

    context = {
        "document":Df,
        "latest_question_list": data_list

    }
    template = loader.get_template("polls/index.html")
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)