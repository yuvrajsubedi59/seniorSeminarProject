from . import views
from django.urls import path



urlpatterns = [
    
    path('', views.Categories, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('event/<slug:slug>/', views.EventDetailView.as_view(), name='eventdetail'),
    path('createevent/', views.CreateEvent.as_view(), name='createvent'),
    path('myevent/',views.Myevents,name='myevent'),
    path('search/' ,views.Search, name='search'),
    path('removeuser/<slug:slug>/<str:id>',views.Removeuser ,name='removeuser'),
    path('eventtype/<int:id>',views.Types, name='types'),
    path('archive/' ,views.Archive, name='archive')

    
    
]