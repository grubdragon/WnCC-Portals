# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from forms import StudentForm, CompanyLoginForm
from models import Student,Tag
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render,reverse,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.utils import timezone

# Create your views here.

@csrf_protect
@login_required
def profile(request):
    name = request.user.first_name +' ' + request.user.last_name
    email = request.user.email
    

    if request.method == 'POST':
        student = get_object_or_404(Student,name=name,email=email,mode_of_login='G')
        form = StudentForm(request.POST, instance=student)
        #return render(request , 'reg.html',{'form':form})
        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))

    
    else:
        try:
            student=Student.objects.get(name=name,email=email,mode_of_login='G')
        except Student.DoesNotExist:
            student = Student.objects.create(name=name,email=email,mode_of_login='G')
        form = StudentForm(instance=student)
        return render(request , 'profile.html',{'student':student})

@csrf_protect
def index(request):
    form = CompanyLoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            #Redirect to student view page
            return HttpResponseRedirect('/admin/portal/student')

    return render(request,'login.html',{'form':CompanyLoginForm})

@login_required
def edit(request):
    name = request.user.first_name +' ' + request.user.last_name
    email = request.user.email
    try:
        student=Student.objects.get(name=name,email=email,mode_of_login='G')
    except Student.DoesNotExist:
        student = Student.objects.create(name=name,email=email,mode_of_login='G')

    if request.method == 'GET':
        form = StudentForm(instance=student)
        tags = Tag.objects.all()
        return render(request , 'form.html',{'student':student,'tags':tags})

