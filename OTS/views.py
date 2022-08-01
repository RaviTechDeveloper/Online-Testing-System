from django.shortcuts import render
from django.http import HttpResponseRedirect
from OTS.models import Question

# Create your views here.
def newQuestion(request):
    res=render(request,'OTS/new_question.html')
    return res
def saveQuestion(request):
    question=Question()
    print(request.POST['question'])
    question.que = request.POST['question']
    question.optiona = request.POST['optiona']
    question.optionb = request.POST['optionb']
    question.optionc = request.POST['optionc']
    question.optiond = request.POST['optiond']
    question.answer = request.POST['answer']
    print(question.que)
    question.save()
    return HttpResponseRedirect('http://localhost:8000/OTS/view_questions/')

def viewQuestions(request):
    questions = Question.objects.all()
    # print(questions)
    print(questions[10].optiona)
    res=render(request,'OTS/view_question.html',{'questions':questions})
    return res