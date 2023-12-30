from django.contrib import admin
from services.models import Services
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_title','service_description')

admin.site.register(Services,ServicesAdmin)