from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('add/', views.add_wishlist_item, name='add_wishlist_item'),
    path('', views.wishlist_view, name='wishlist'),
    path('edit/<int:item_id>/', views.edit_wishlist_item, name='edit_wishlist_item'),
    path('delete/<int:item_id>/', views.delete_wishlist_item, name='delete_wishlist_item'),
]