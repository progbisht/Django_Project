from django.contrib import admin
from team.models import Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'description', 'twitter_icon', 'insta_icon', 'facebook_icon', 'linkedin_icon', 'image')

admin.site.register(Team,TeamAdmin)