from django import forms
from .models import Events
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):
    
    class Meta:
        model = Events
        fields = ("eventt","slug","date","time","discord_link","location","maps_url")
        widgets = {
            'date': forms.DateInput(attrs={'type':"date"}),
            'time' :forms.TimeInput(attrs={'type':'time'}),
            'discord_link':forms.URLInput(attrs={'required':'false'}),
            'slug':forms.TextInput(attrs={'class':'form-control mb-3'})
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "First name")

    class Meta:
        model = User
        fields = ("username", "first_name","last_name", "email", )
        