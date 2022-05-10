from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from petstagram.common.helpers import BootsTrapMixin, DisableFieldsMixin
from petstagram.main.models import Pet


class CreatePetForm(forms.ModelForm, BootsTrapMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        pet = super().save(commit=False)

        pet.user = self.user
        if commit:
            pet.save()

        return pet

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter pet name'})
        }

class EditPetForm(forms.ModelForm, BootsTrapMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')


class DeletePetForm(forms.ModelForm, BootsTrapMixin, DisableFieldsMixin):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self._init_bootstrap_form_controls()
    #
    #     self._init_disable_fields()

    def save(self, commit=True):
        # photos = PetPhoto.objects.filter(tagged_pet=self.instance)
        # print(photos)
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        fields = ()






