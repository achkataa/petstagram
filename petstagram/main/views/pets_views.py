from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from petstagram.main.forms.pet_forms import CreatePetForm, EditPetForm, DeletePetForm
from petstagram.main.models import Pet


class CreatePetView(CreateView):
    template_name = 'main/pet_create.html'
    form_class = CreatePetForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class EditPetView(UpdateView):
    model = Pet
    template_name = 'main/pet_edit.html'
    form_class = EditPetForm

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.user_id})



class DeletePetView(DeleteView):
    model = Pet
    template_name = 'main/pet_delete.html'
    form_class = DeletePetForm
    success_url = reverse_lazy('dashboard')
