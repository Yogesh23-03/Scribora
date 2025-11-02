from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']

class DateInput(forms.DateInput):
    input_type='date'



class HomeworkForm(forms.ModelForm):
    class Meta:
        model=Homework
        widgets={'due':DateInput()}
        #widgets={'due':forms.DateInput(attrs={'class':'form-control','type':'date'})}
        fields=['subject','title','description','due','is_finished']


class DashboardForm(forms.Form):
    text=forms.CharField(max_length=400,label="Enter Your Search")


class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','is_finished']

class Conversion(forms.Form):
    CHOICES = [('length', 'Length'), ('mass', 'Mass')]
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


class ConversionLength(forms.Form):
    CHOICES = [
        ('yard', 'Yard'),
        ('foot', 'Foot'),
        ('meter', 'Meter'),
        ('centimeter', 'Centimeter'),
        ('inch', 'Inch'),
    ]
    input = forms.FloatField(required=False, label=False, widget=forms.TextInput(
        attrs={ 'placeholder': 'Enter the Number'}
    ))
    measure1 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))
    measure2 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))


class ConversionMass(forms.Form):
    CHOICES = [
        ('pound', 'Pound'),
        ('kilogram', 'Kilogram'),
        ('gram', 'Gram'),
        ('ounce', 'Ounce'),
    ]
    input = forms.FloatField(required=False, label=False, widget=forms.TextInput(
        attrs={ 'placeholder': 'Enter the Number'}
    ))
    measure1 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))
    measure2 = forms.CharField(label='', widget=forms.Select(choices=CHOICES))

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']