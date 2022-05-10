from django.urls import path

from petstagram.main.views.generic import HomePageView, DashboardView
from petstagram.main.views.pets_views import CreatePetView, EditPetView, DeletePetView
from petstagram.main.views.photo_views import PhotoDetailsView, like_pet_photo, CreatePhotoView, EditPhotoView, \
    DeletePhotoView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('photo/details/<int:pk>/', PhotoDetailsView.as_view(), name='photo_details'),
    path('photo/like/<int:pk>', like_pet_photo, name='like_pet_photo'),
    path('photo/add', CreatePhotoView.as_view(), name='add_photo'),
    path('photo/edit/<int:pk>', EditPhotoView.as_view(), name='edit_photo'),
    path('phoyo/delete/<int:pk>', DeletePhotoView.as_view(), name='delete_photo'),

    path('pet/add/', CreatePetView.as_view(), name='add_pet'),
    path('pet/edit/<int:pk>', EditPetView.as_view(), name='edit_pet'),
    path('pet/delete/<int:pk>', DeletePetView.as_view(), name='delete_pet'),




]
