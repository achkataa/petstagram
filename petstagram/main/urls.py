from django.urls import path

from petstagram.main.views.generic import home_page_view, dashboard_view
from petstagram.main.views.pets_views import add_pet, edit_pet, delete_pet
from petstagram.main.views.photo_views import photo_details_view, like_pet_photo, add_photo, edit_photo
from petstagram.main.views.profile_views import profile_view, create_profile, edit_profile, delete_profile

urlpatterns = [
    path('', home_page_view, name='home_page'),
    path('dashboard/', dashboard_view, name='dashboard'),

    path('photo/details/<int:pk>/', photo_details_view, name='photo_details'),
    path('photo/like/<int:pk>', like_pet_photo, name='like_pet_photo'),
    path('photo/add', add_photo, name='add_photo'),
    path('photo/edit/<int:pk>', edit_photo, name='edit_photo'),

    path('profile/', profile_view, name='profile'),
    path('profile/create/', create_profile, name='create_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/delete/', delete_profile, name='delete_profile'),

    path('pet/add/', add_pet, name='add_pet'),
    path('pet/edit/<int:pk>', edit_pet, name='edit_pet'),
    path('pet/delete/<int:pk>', delete_pet, name='delete_pet'),




]
