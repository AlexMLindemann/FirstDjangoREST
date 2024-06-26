from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import viewsets
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("FirstApp/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer