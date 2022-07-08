from xml.parsers.expat import model
from django.contrib import admin

from apps.core.models import Contact, Feedback,PopularClients
admin.site.site_header = "Nation Electronics Admin"
admin.site.site_title = "Welcome to Nation Electronics Admin"
admin.site.index_title = "Welcome to Nation Electronics Admin"
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name','feedback','date')
class PopularClientsAdmin(admin.ModelAdmin):
    list_display = ('client_name','ratting')
admin.site.register(Contact,ContactAdmin)
# admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(PopularClients,PopularClientsAdmin)