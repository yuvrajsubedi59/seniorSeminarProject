from django.contrib import admin
from .models import   Events,EventType

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventt', 'slug', 'date', 'organizer')
    search_fields = ['eventt', 'date',]
    prepopulated_fields = {'slug': ('eventt',)}

admin.site.register(Events,EventAdmin)
admin.site.register(EventType)

# Register your models here.
