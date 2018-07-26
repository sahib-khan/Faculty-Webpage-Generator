from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile , course, department,Deg
from django.conf import settings
from captcha.fields import ReCaptchaField

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class EditProfileForm(forms.Form):
    title = forms.CharField(max_length=10,required=False)
    fname = forms.CharField(max_length=200,required=False)
    mname = forms.CharField(max_length=200,required=False)
    lname = forms.CharField(max_length=200,required=False)
    email = forms.EmailField(max_length=200,required=False)
    dep = forms.ModelChoiceField(queryset=department.objects.all())
    desig = forms.CharField(max_length=200,required=False)
    descrip = forms.CharField(max_length=500,widget=forms.Textarea,required=False)
    office = forms.CharField(max_length=50,required=False)
    phn_no = forms.CharField(max_length=200,required=False)
    resid = forms.CharField(max_length=200,required=False)

class addCourse(forms.Form):
    startYear = forms.IntegerField()
    endYear = forms.IntegerField()
    semester = forms.CharField(max_length=4)
    name = forms.CharField(max_length=200)
    course_code = forms.CharField(max_length=6)

class delcourse(forms.Form):
    del_course = forms.ModelChoiceField(queryset=course.objects.all())

class eduForm(forms.Form):
    college = forms.CharField(max_length=200)
    degree = forms.CharField(max_length=50)
    descrip = forms.CharField(max_length=200,widget=forms.Textarea)
    startTime = forms.CharField(max_length=50)
    endTime = forms.CharField(max_length=50)

class exForm(forms.Form):
    desig =forms.CharField(max_length=200)
    firm = forms.CharField(max_length=200)
    descrip = forms.CharField(max_length=200,widget=forms.Textarea)
    startTime = forms.CharField(max_length=50)
    endTime = forms.CharField(max_length=50)

class resIntform(forms.Form):
    descrip = forms.CharField(max_length=200,widget=forms.Textarea)

class pubForm(forms.Form):
    descrip = forms.CharField(max_length=500,widget=forms.Textarea)

class bookForm(forms.Form):
    descrip = forms.CharField(max_length=500,widget=forms.Textarea)

class conForm(forms.Form):
    degree = forms.ModelChoiceField(queryset=Deg.objects.all())
    name = forms.CharField(max_length=200)

class comForm(forms.Form):
    degree = forms.ModelChoiceField(queryset=Deg.objects.all())
    name = forms.CharField(max_length=200)
    supervisor = forms.CharField(max_length=200)
    thesisTitle = forms.CharField(max_length=200)

class proForm(forms.Form):
    title = forms.CharField(max_length=200)
    PI = forms.CharField(max_length=200)
    FundingAgency = forms.CharField(max_length=200)
    syear = forms.IntegerField()
    fyear = forms.IntegerField()

class awdForm(forms.Form):
    descrip = forms.CharField(max_length=500)
