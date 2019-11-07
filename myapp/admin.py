from django.contrib import admin
from . models import  profile
# Register your models here.
class profileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthdate', 'fathername', 'mothername', 'photo')
admin.site.register(profile, profileAdmin)
