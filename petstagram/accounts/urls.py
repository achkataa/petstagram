from django.urls import path

from petstagram.accounts.views import LoginUserView, ProfileView, RegisterUserView, EditUserView, DeleteUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/create/', RegisterUserView.as_view(), name='create_profile'),
    path('profile/edit/<int:pk>/', EditUserView.as_view(), name='edit_profile'),
    path('profile/delete/<int:pk>/', DeleteUserView.as_view(), name='delete_profile'),
]