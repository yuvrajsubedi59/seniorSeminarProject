from django import forms
from .models import Events
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):
    
    class Meta:
        model = Events
        fields = ("eventt","slug","date","location","organizer")
        widgets = {
            'date': forms.DateInput(attrs={'type':"date"})
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "First name")

    class Meta:
        model = User
        fields = ("username", "first_name","last_name", "email", )
        