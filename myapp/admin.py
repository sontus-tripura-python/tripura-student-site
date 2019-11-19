from django.contrib import admin
from . models import  Profile, News, leadership, about, SubLeader
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fathername', 'mothername', 'photo')
admin.site.register(Profile, ProfileAdmin)
admin.site.register(News)
admin.site.register(leadership)
admin.site.register(about)
admin.site.register(SubLeader)
