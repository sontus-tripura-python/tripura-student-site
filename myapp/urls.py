from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('accoount/edit/', views.accoount_update, name='accoount_update'),
]
