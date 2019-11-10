from django.urls import path
from . import views
urlpatterns = [
    path('', views.tripura, name='tripura'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('accoount/edit/', views.accoount_update, name='accoount_update'),
    path('news/', views.News_list, name='News_list'),
    path('news/<int:pk>/', views.news_details, name='news_details'),
    path('leader/', views.leadership, name='leadership'),
    path('members/', views.Membership , name='Membership'),
    #path('members/<int:>/', views.view_profile, name='view_profile'),
    ]
