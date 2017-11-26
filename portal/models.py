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

    name = models.CharField(max_length=50)
    college_name = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()
    year = models.IntegerField()
    resume = models.URLField()
    github = models.URLField()
    stackoverflow = models.URLField()
    work_experience = models.TextField()
    about =  models.TextField()
    interests = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name
    
