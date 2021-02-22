from django.http.response import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import face_recognition
from . import forms, urls
from .models import Group, Member
from PIL import Image
import numpy as np
import base64
import random
from io import BytesIO
# Create your views here.
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def index(request):
    return render(request, 'index.html')


def create_count(request):
    if request.method == 'POST':
        form = forms.CreateCountForm(request.POST)
        if form.is_valid():
            member_count = form.cleaned_data['count']
            return redirect('create', member_count=member_count)
    else:
        form = forms.CreateCountForm()

    return render(request, 'create-count.html', {'form': form})


def create_success(request, group_id=None):
    if group_id != None:
        return render(request, 'create_success.html', context={'group_id': group_id})
    else:
        raise Http404


def create(request, member_count=None):
    member_count = int(member_count)
    if member_count == None:
        print('no member count')
        raise Http404
    if request.method == 'POST':
        form = forms.CreateForm(
            request.POST, request.FILES, member_count=member_count)
        if form.is_valid():
            object_list = []
            error_raised = False
            # do this before and save it

            # get the group id
            group_id = ''
            for i in range(7):
                group_id += letters[random.randint(0, 61)]
            # get the meeting url
            meeting_url = form.cleaned_data['meeting_url']
            group = Group(
                group_id=group_id, meeting_url=meeting_url)
            object_list.append(group)
            # take care of getting member count
            for i in range(member_count):
                name = form.cleaned_data[f'name_{i}']

                image = form.cleaned_data[f'image_{i}']
                try:
                    person = (face_recognition.face_encodings(
                        face_recognition.load_image_file(image))[0])
                except:
                    form.add_error(f'image_{i}', ValidationError(
                        _('Please enter a human face!'), code='invalid'))
                    error_raised = True
                    continue
                string_person = base64.binascii.b2a_base64(
                    person).decode("ascii")

                member = Member(
                    name=name, encoded_file=string_person, group=group)
                object_list.append(member)
            if not error_raised:
                for model in object_list:
                    model.save()
                return redirect('create-success', group_id=group_id)

    else:
        form = forms.CreateForm(member_count=member_count)
    return render(request, 'create.html', {'form': form})


def join(request):
    if request.method == 'POST':
        form = forms.JoinForm(request.POST)

        if form.is_valid():
            group_id = form.cleaned_data['group_id']
            name = form.cleaned_data['name']
            image_64 = form.cleaned_data['image']

            image = BytesIO(base64.b64decode(image_64))
            try:
                group = Group.objects.filter(group_id__exact=group_id)[0]
            except:
                return redirect('join-failed')
            members = group.member_set.all()
            matching_names = members.filter(name__exact=name)
            try:
                user = face_recognition.face_encodings(
                    face_recognition.load_image_file(image))[0]
            except:
                return redirect('join-failed')
            for i in matching_names:
                test = np.frombuffer(base64.binascii.a2b_base64(
                    i.encoded_file.encode("ascii")))
                if face_recognition.compare_faces([test], user):
                    face_distances = face_recognition.face_distance(
                        [test], user)
                    face_match_percentage = (1 - face_distances) * 100
                    for i, face_distance in enumerate(face_distances):
                        print("The test image has a distance of {:.2} from known image #{}".format(
                            face_distance, i))

                        print(
                            "- comparing with a tolerance of 0.6? {}".format(face_distance < 0.6))

                        x = np.round(face_match_percentage, 4)
                        print(x)
                        if x > 55:
                            return redirect(f'{group.meeting_url}')
            return redirect('join-failed')
    else:
        form = forms.JoinForm()

    return render(request, 'join.html', {'form': form})


def join_failed(request):
    return render(request, 'join-failed.html')
