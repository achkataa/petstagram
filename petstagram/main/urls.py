from django.urls import path

from petstagram.main.views import home_page_view, dashboard_view, profile_view, photo_details_view, like_pet_photo

urlpatterns = [
    path('', home_page_view, name='home_page'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_view, name='profile'),
    path('photo/details/<int:pk>/', photo_details_view, name='photo_details'),
    path('photo/like/<int:pk>', like_pet_photo, name='like_pet_photo'),
]
