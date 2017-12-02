# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import StudentForm
from models import Student
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render,reverse,redirect

# Create your views here.

@login_required
def profile(request):
    name = request.user.first_name +' ' + request.user.last_name
    email = request.user.email
    try:
        student=Student.objects.get(name=name,email=email,mode_of_login='G')
    except Student.DoesNotExist:
        student = Student.objects.create(name=name,email=email,mode_of_login='G')

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student) 
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))

    
    else:
        form = StudentForm(instance=student)
        return render(request , 'profile.html',{'student':student})

def index(request):
    return render(request,'login.html')
