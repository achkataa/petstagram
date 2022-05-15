from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from petstagram.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.accounts.models import Profile, PetstagramUser
from petstagram.common.helpers import get_profile
from petstagram.main.models import Pet, PetPhoto


class RegisterUserView(CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(LoginView):
    template_name = 'accounts/login_page.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')

        return super().dispatch(request, *args, **kwargs)


class EditUserView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'accounts/profile_edit.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.user_id})


class DeleteUserView(DeleteView):
    model = get_user_model()
    form_class = DeleteProfileForm
    template_name = 'accounts/profile_delete.html'
    success_url = reverse_lazy('home_page')





class ChangePasswordView():
    pass




class ProfileView(DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'info'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pets = Pet.objects.filter(user_id=self.object.user_id)
        photos = PetPhoto.objects.filter(user_id=self.object.user_id).distinct()
        pets_photos_count = len(photos)
        pets_photos_likes = sum([photo.likes for photo in photos])
        context.update({
            'pets_photos_count': pets_photos_count,
            'pets_photos_likes': pets_photos_likes,
            'is_owner': self.object.user_id == self.request.user.id,
            'pets': pets,
        })
        return context