# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Student,Tag

# Register your models here.

class StudentAdmin(admin.ModelAdmin):

    def get_readonly_fields(self,request,obj=None):
        if obj:
            return ('name','email')

admin.site.register(Student,StudentAdmin)
admin.site.register(Tag)
