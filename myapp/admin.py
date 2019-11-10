from django.contrib import admin
from . models import  profile, Post, leadership
# Register your models here.
class profileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthdate', 'fathername', 'mothername', 'photo')
admin.site.register(profile, profileAdmin)
admin.site.register(Post)
admin.site.register(leadership)
