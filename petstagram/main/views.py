from django.shortcuts import render, redirect

# Create your views here.
from petstagram.main.models import Profile, PetPhoto


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

def get_photo_information(arg=None):
    profile = get_profile()
    if arg == "Count":
        return PetPhoto.objects.filter(tagged_pets__user_profile=profile).count()
    else:
        photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile)
        return sum([photo.likes for photo in photos])



def home_page_view(request):
    context = {
        'hide_adititonal_nav_items': True
    }
    return render(request, 'main/home_page.html', context)

def dashboard_view(request):
    profile = get_profile()
    pets_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile)
    context = {
        'pets_photos': pets_photos
    }
    return render(request, 'main/dashboard.html', context)

def profile_view(request):
    pets_photos_count = get_photo_information('Count')
    pets_photos_likes = get_photo_information()
    profile_pk = get_profile().pk
    info = Profile.objects.get(pk=profile_pk)
    context = {
        'info': info,
        'pets_photos_count': pets_photos_count,
        'pets_photos_likes': pets_photos_likes,
    }
    return render(request, 'main/profile_details.html', context)

def photo_details_view(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    context = {
        'pet_photo': pet_photo
    }
    return render(request, 'main/photo_details.html', context)

def like_pet_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    photo.likes += 1
    photo.save()
    return redirect('photo_details', pk)