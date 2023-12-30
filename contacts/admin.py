from django.contrib import admin
from contacts.models import Contacts
# Register your models here.

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('contact_name','contact_email','contact_subject', 'contact_message')

admin.site.register(Contacts,ContactsAdmin)