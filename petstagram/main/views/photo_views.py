from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from petstagram.accounts.models import Profile
from petstagram.main.forms.photos_forms import CreatePhotoForm, EditPhotoForm
from petstagram.main.models import PetPhoto

#
# def photo_action(request, model_form, redirect_url_name, instance, template_name):
#     if request.method == "POST":
#         form = model_form(request.POST, request.FILES, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect(redirect_url_name)
#     else:
#         form = model_form(instance=instance)
#     context = {
#         'form': form,
#         'photo': instance
#     }
#     return render(request, template_name, context)

class CreatePhotoView(CreateView):
    template_name = 'main/photo_create.html'
    form_class = CreatePhotoForm
    success_url = reverse_lazy('dashboard')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class EditPhotoView(UpdateView):
    model = PetPhoto
    form_class = EditPhotoForm
    template_name = 'main/photo_edit.html'
    success_url = reverse_lazy('dashboard')


class PhotoDetailsView(DetailView):
    model = PetPhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'pet_photo'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        last_viewed_pet_photos = request.session.get('last_viewed_pet_photos', [])

        last_viewed_pet_photos.insert(0, self.kwargs['pk'])

        request.session['last_viewed_pet_photos'] = last_viewed_pet_photos[:4]

        return response

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context

class DeletePhotoView(DeleteView):
    model = PetPhoto
    template_name = 'main/photo_delete.html'
    success_url = reverse_lazy('dashboard')


def like_pet_photo(request, pk):
    has_liked_photo = None
    if request.session.get('has_liked_photo', False):
        has_liked_photo = True

    request.session['has_liked_photo'] = True
    context = {
        'has_liked_photo'
    }

    return redirect('photo_details', pk)