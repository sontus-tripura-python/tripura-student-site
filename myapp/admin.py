from django.contrib import admin
from . models import  profile, News, leadership
# Register your models here.
class profileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthdate', 'fathername', 'mothername', 'photo')
admin.site.register(profile, profileAdmin)
admin.site.register(News)
admin.site.register(leadership)
