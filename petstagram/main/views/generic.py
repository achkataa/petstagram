from django.shortcuts import render

from petstagram.main.helpers import get_profile
from petstagram.main.models import PetPhoto


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

def handle_404(request):
    return render(request, 'main/401_error.html')