from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def create(request):
    return render(request, 'create.html')


def join(request):
    return render(request, 'join.html')
