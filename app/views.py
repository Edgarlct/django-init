from django.shortcuts import render, redirect

# Create your views here.
from .models import Questions


def index(request):
    questions = Questions.objects.all()
    return render(request, 'app/index.html',{'questions':questions})

def delete(request, question_id):
    question = Questions.objects.get(id=question_id)
    question.delete()
    return redirect('app:index')

def post(request):
    question = Questions(text=request.POST['question'])
    question.save()
    return redirect('app:index')

def detail(request, question_id):
    question = Questions.objects.get(id=question_id)
    return render(request, 'app/detail.html', {'question':question})

def put(request, question_id):
    question = Questions.objects.get(id=question_id)
    question.text = request.POST['question']
    question.save()
    return redirect('app:index')

