from django.shortcuts import render, redirect

from petstagram.main.forms.pet_forms import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.main.helpers import get_profile
from petstagram.main.models import Pet

def pet_action(request, model_form, redirect_url_name, instance, template_name):
    if request.method == "POST":
        form = model_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_url_name)
    else:
        form = model_form(instance=instance)
    context = {
        'form': form,
        'pet': instance,
    }
    return render(request, template_name, context)



def add_pet(request):
    return pet_action(request, CreatePetForm, 'profile', Pet(user_profile=get_profile()), 'main/pet_create.html')


def edit_pet(request, pk):
    return pet_action(request, EditPetForm, 'profile', Pet.objects.get(pk=pk), 'main/pet_edit.html')

def delete_pet(request, pk):
    return pet_action(request, DeletePetForm, 'profile', Pet.objects.get(pk=pk), 'main/pet_delete.html')