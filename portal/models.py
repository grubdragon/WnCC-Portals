# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tag(models.Model):

    gig = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.gig
    

class Student(models.Model):

    YEAR_CHOICES=[(c,c) for c in [1,2,3,4,5]]
    PROGRAM_CHOICES=[(c,c) for c in['Bachelors','Masters','Doctorate','Post-Doctorate']]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mode_of_login = models.CharField(max_length=10,default='SSO')
    college_name = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()
    year = models.IntegerField(choices=YEAR_CHOICES)
    programme_of_study = models.CharField(max_length=20,choices=PROGRAM_CHOICES,null=True)
    resume = models.URLField(blank=True)
    github = models.URLField(blank=True)
    stackoverflow = models.URLField(blank=True)
    work_experience = models.TextField(blank=True)
    about =  models.TextField(blank=True)
    interests = models.ManyToManyField(Tag)
    avaiable = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name
    
