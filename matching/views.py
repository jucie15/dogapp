from django.shortcuts import render
from matching.forms import ProfileForm
import os

def index(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,
            request.FILES)
        if form.is_valid():
            profile = form.save()
    else:
        form = ProfileForm()

    return render(request, 'matching/index.html', {
            'form' : form,
        })
