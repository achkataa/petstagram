from django.shortcuts import render, redirect

from petstagram.main.forms.profile_forms import CreateProfileForm, EditProfileForm, DeleteProfile
from petstagram.main.helpers import get_profile
from petstagram.main.models import PetPhoto, Profile, Pet


def profile_view(request):
    profile = get_profile()
    pets = Pet.objects.filter(user_profile=profile)
    photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct()
    pets_photos_count = len(photos)
    pets_photos_likes = sum([photo.likes for photo in photos])
    context = {
        'info': profile,
        'pets_photos_count': pets_photos_count,
        'pets_photos_likes': pets_photos_likes,
        'pets': pets
    }
    return render(request, 'main/profile_details.html', context)

def profile_action(request, model_form, redirect_url_name, instance, template_name):
    if request.method == "POST":
        form = model_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_url_name)
    else:
        form = model_form(instance=instance)
    context = {
        'form': form,
    }
    return render(request, template_name, context)




def create_profile(request):
    return profile_action(request, CreateProfileForm, 'home_page', Profile(), 'main/profile_create.html')


def edit_profile(request):
    return profile_action(request, EditProfileForm, 'profile', get_profile(), 'main/profile_edit.html')

def delete_profile(request):
    return profile_action(request, DeleteProfile, 'home_page', get_profile(), 'main/profile_delete.html')