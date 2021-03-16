from django import forms
from .models import Events

class EventForm(forms.ModelForm):
    
    class Meta:
        model = Events
        fields = ("eventt","slug","date","location","organizer")
        widgets = {
            'date': forms.DateInput(attrs={'type':"date"})
        }
