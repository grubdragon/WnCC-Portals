from django import forms
from django.contrib.auth.models import User
from models import Student,Tag
from django.utils.translation import ugettext_lazy as _
 
 #Form for  Registration
class RegistrationForm(forms.Form):
    
    name = forms.CharField( widget=forms.TextInput(attrs=dict(required=True, max_length=50)), label="Name", error_messages={ 'invalid': _("This value must contain only letters.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)), label="Email address")
    college_name = forms.CharField( widget=forms.TextInput(attrs=dict(required=True, max_length=200)), label="College", error_messages={ 'invalid': _("This value must contain only letters.") })
    contact = forms.CharField( widget=forms.TextInput(attrs=dict(required=True, max_length=10)), label="Primary Contact Number", error_messages={ 'invalid': _("This value must contain only letters.") })
    year = forms.ChoiceField(
            choices = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5')),
            widget = forms.RadioSelect,
        )

    programme = forms.ChoiceField(
            choices = (('Bachelors','1'),('Masters','2'),('Doctorate','3'),('Post-Doctorate','4')),
            widget = forms.RadioSelect,
        )

    resume_link = forms.URLField(label='Link to your Resume',required=False)
    github_link = forms.URLField(label='Link to your Github Profile',required=False)
    so_link = forms.URLField(label='Link to your StackOverflow Profile',required=False)
    work_experience = forms.CharField(widget=forms.Textarea,required=False)
    about = forms.CharField(widget=forms.Textarea,required=False)
    interests = forms.MultipleChoiceField(choices=Tag.objects.all(), widget=forms.CheckboxSelectMultiple,
    )
    '''
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            print self.cleaned_data['password1']
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

#Form for search in excel
class SearchForm(forms.Form):
    number = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,type='number')),label = ("Input"))

    def clean(self):
        if 'number' in self.cleaned_data:
            if ( len(self.cleaned_data['number']) != 6):
                raise forms.ValidationError(_("Enter a 6 digit number only"))
        return self.cleaned_data
        '''


class StudentForm(forms.ModelForm):
    interests = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    class Meta:

        model = Student
        exclude = ['mode_of_login','available']
        
    