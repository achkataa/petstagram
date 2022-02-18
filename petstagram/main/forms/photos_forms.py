from django import forms

from petstagram.main.helpers import BootsTrapMixin
from petstagram.main.models import PetPhoto


class CreatePhotoForm(forms.ModelForm, BootsTrapMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

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



