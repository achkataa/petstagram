from django import forms

from petstagram.common.helpers import BootsTrapMixin
from petstagram.main.models import PetPhoto


class   CreatePhotoForm(forms.ModelForm, BootsTrapMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        photo = super().save(commit=False)

        photo.user = self.user
        if commit:
            photo.save()

        return photo


    class Meta:
        model = PetPhoto
        fields = ('photo','description', 'tagged_pets')

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': ' Enter description', 'rows': 3}),
        }

class EditPhotoForm(forms.ModelForm, BootsTrapMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = PetPhoto
        fields = ('description', 'tagged_pets')

        widgets = {
            'description': forms.Textarea(attrs={'rows': 3})
        }

class DeletePhotoForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ()



