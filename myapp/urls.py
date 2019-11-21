from django.urls import path
from . import views
urlpatterns = [
    path('', views.tripura, name='tripura'),
    path('about/', views.about_list, name='about_list'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/', views.profile, name='profile_with_pk'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('accoount/edit/', views.accoount_update, name='accoount_update'),
    path('news/', views.News_list, name='News_list'),
    path('news/<int:pk>/', views.news_details, name='news_details'),
    path('leader/', views.leader_list, name='leader_list'),
    path('leader/<int:pk>/', views.leader_details, name='leader_details'),
    path('subleader/', views.subleader_list, name='subleader_list'),
    path('subleader/<int:pk>/', views.subleader_details, name='subleader_details'),
    path('members/', views.Membership , name='Membership'),
    #path('members/<int:>/', views.view_profile, name='view_profile'),
    ]
