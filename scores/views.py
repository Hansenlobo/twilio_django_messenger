from django.shortcuts import render,redirect
from .forms import  ScoreForm
# Create your views here.
from .models import *


def index(request):
    task=Score.objects.all()
    form=ScoreForm()
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {
        'tasks':task,
        'form': form
    }
    return render(request,'scores/index.html',context)