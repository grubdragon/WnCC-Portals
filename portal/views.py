# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import StudentForm
from models import Student
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render

# Create your views here.
@login_required
def register(request):
    pk = request.user
    instance = get_object_or_404(Student, id=pk)
    
    if request.method == 'POST': #It is better to explicitly check for method instead of the dictionary
        form = StudentForm(request.POST, instance=instance) #No need of the 
        if form.is_valid():
            form.save()
            return render(request , 'registration/register.html',{'form':form})

    
    else:
        form = StudentForm(instance=instance)
        return render(request , 'registration/register.html',{'form':form})
