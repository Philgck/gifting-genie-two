from django.urls import path
from . import views

app_name = 'friendslist'

urlpatterns = [
    path('', views.friendship_list, name='friendslist'),
    path('confirm/<int:friendship_id>/',
        views.confirm_friendship, name='confirm_friendship'),
    path('search-usernames/', views.search_usernames, name='search-usernames'),
]
