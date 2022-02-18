from django.shortcuts import render, redirect

from petstagram.main.forms.photos_forms import CreatePhotoForm, EditPhotoForm
from petstagram.main.models import PetPhoto


def photo_action(request, model_form, redirect_url_name, instance, template_name):
    if request.method == "POST":
        form = model_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_url_name)
    else:
        form = model_form(instance=instance)
    context = {
        'form': form,
        'photo': instance
    }
    return render(request, template_name, context)

def add_photo(request):
    return photo_action(request, CreatePhotoForm, 'dashboard', PetPhoto(), 'main/photo_create.html')

def edit_photo(request, pk):
    return photo_action(request, EditPhotoForm, 'dashboard', PetPhoto.objects.get(pk=pk), 'main/photo_edit.html')


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