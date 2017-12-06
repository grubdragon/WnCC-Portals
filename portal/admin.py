# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Student,Tag

# Register your models here.

class StudentAdmin(admin.ModelAdmin):

    list_display=('name','college','email','contact_no')
    list_filter=['college','interests']
    #filter_horizontal=['interests']
    
    def has_delete_permission(self,request,obj=None):
        
        if request.user.is_superuser:
            return True
        else :
            return False
        
    def get_readonly_fields(self,request,obj=None):
        
        if obj: 
            print 'here'
            if not request.user.is_superuser:
                return list(self.readonly_fields) + \
                    [field.name for field in obj._meta.fields] + \
                    [field.name for field in obj._meta.many_to_many]

            return ('name','email')
        return []

admin.site.register(Student,StudentAdmin)
admin.site.register(Tag)
