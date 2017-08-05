from django.shortcuts import render, get_object_or_404, redirect
from matching.forms import ProfileForm
from matching.models import Profile
from dog.main import human_or_dog
import os

def index(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,
            request.FILES)
        if form.is_valid():
            profile = form.save()
            dog_name, dog_value = human_or_dog(profile.upload_image)
            profile.save_profile(dog_name, dog_value)
            return redirect(profile)
    else:
        form = ProfileForm()

    return render(request, 'matching/index.html', {
            'form' : form,
        })

def result(request, pk):
    profile = get_object_or_404(Profile, pk=pk)

    return render(request, 'matching/result.html', {
            'profile' : profile,
        })

