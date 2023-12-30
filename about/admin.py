from django.contrib import admin
from about.models import About
# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading', 'title', 'description')

admin.site.register(About,AboutAdmin)