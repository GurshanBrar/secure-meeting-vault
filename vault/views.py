from django.shortcuts import render, redirect
import face_recognition
from . import forms

# Create your views here.


def index(request):
    return render(request, 'index.html')


def create_success(request, group_id):
    return render(request, 'create_success.html', context={'group_id': group_id})


def create(request):
    if request.method == 'POST':
        form = forms.CreateForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data())
            group_id = 444
            # do further validation if needed, but we can worry about that later
            # first generate a group id
            # do val
            # heres where we update the databse and encode the images and such, charan
            return redirect('create_success', group_id=group_id)
    else:
        form = forms.CreateForm()

    return render(request, 'create.html', {'form': form})


def join(request):
    return render(request, 'join.html')
