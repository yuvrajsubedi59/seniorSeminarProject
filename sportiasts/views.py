from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect,reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import EventForm, RegisterForm
from . import models
# Create your views here.

def Categories(request):
    template = loader.get_template('sportiasts/home.html')
    events = models.Events.objects.all()
    return HttpResponse(template.render({'events':events},request))


class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CreateEvent(generic.CreateView):
    form_class = EventForm
    success_url = reverse_lazy('home')
    template_name = 'sportiasts/createevent.html'

class EventDetailView(generic.DetailView):
    model = models.Events
    template_name='sportiasts/eventdetail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["players"] = self.get_object().player.all()
        return context
    

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed

        if self.request.GET.get('csrfmiddlewaretoken'):
            print(request.user)
            print(self.get_object().player.all())
            self.get_object().player.add(request.user)
        return handler(request, *args, **kwargs)
   
    
            