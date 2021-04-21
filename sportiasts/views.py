from django.views import generic
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect,reverse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import EventForm, RegisterForm
from django.contrib.auth.models import User
from . import models
from datetime  import date as d
from django.db.models import Q

# Create your views here.

def Categories(request):
    template = loader.get_template('sportiasts/home.html')
    events = models.Events.objects.all().reverse()
    return HttpResponse(template.render({'events':events},request))

def Search(request):
    template = loader.get_template('sportiasts/search.html')
    q = request.GET['q']
    events = models.Events.objects.filter(
        eventt__icontains=q).order_by('date').reverse() | models.Events.objects.filter(
        location__icontains=q).order_by('date').reverse() | models.Events.objects.filter(
        EventType__title__icontains=q).order_by('date').reverse()
    print(events.count())
    if events.count()==0:
        empty=True
    else:
        empty = False
    return HttpResponse(template.render({'events':events,'q':q, 'empty':empty},request))


def Myevents(request):
    template = loader.get_template('sportiasts/myevents.html')
    user = request.user
    print(user.players.all())
    events = user.players.all()
    return HttpResponse(template.render({'events':events,"user":user},request))

def Archive(request):
    template = loader.get_template('sportiasts/archive.html')
    events = models.Events.objects.all().order_by('date')
    return HttpResponse(template.render({'events':events,},request))

def Types(request,id):
    template = loader.get_template('sportiasts/types.html')
    types = models.EventType.objects.get(pk=id)
    print(types)
    events = models.Events.objects.filter(EventType=types).order_by('date').reverse()
    return HttpResponse(template.render({'eventtype':types,"events":events},request))

def Removeuser(request,slug,id):
    template = loader.get_template('sportiasts/removeuser.html')
    event = models.Events.objects.filter(slug=slug)
    user = User.objects.filter(username=id)
    print(event[0],user[0])
    event[0].player.remove(user[0])
    return HttpResponse(template.render({'events':event[0],"user":user[0]},request))


class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CreateEvent(generic.CreateView):
    form_class = EventForm
    success_url = reverse_lazy('home')
    template_name = 'sportiasts/createevent.html'

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        form.save()
        return redirect('home')

class EventDetailView(generic.DetailView):
    model = models.Events
    template_name='sportiasts/eventdetail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["players"] = self.get_object().player.all()
        print(self.request.user in context['players'])
        if self.request.user in context['players']:
            context['join']=False
        else:
            context['join']=True
        return context
    

    def dispatch(self, request, *args, **kwargs):
        print(self.http_method_names)
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed


        if self.request.GET.get('join'):
            print(request.user)
            print(self.get_object().player.all())
            self.get_object().player.add(request.user)

        elif self.request.GET.get('withdraw'):
            self.get_object().player.remove(request.user)
        return handler(request, *args, **kwargs)
   
    
            