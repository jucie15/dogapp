from django.shortcuts import render
from matching.forms import ProfileForm
from dog.main import human_or_dog
import os

def index(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,
            request.FILES)
        if form.is_valid():
            profile = form.save()
            human_or_dog(profile.upload_image)
    else:
        form = ProfileForm()

    return render(request, 'matching/index.html', {
            'form' : form,
        })
