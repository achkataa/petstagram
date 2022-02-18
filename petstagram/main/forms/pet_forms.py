from datetime import date

from django import forms
from django.core.exceptions import ValidationError

from petstagram.main.helpers import BootsTrapMixin, DisableFieldsMixin
from petstagram.main.models import Pet, PetPhoto


class CreatePetForm(forms.ModelForm, BootsTrapMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter pet name'})
        }

class EditPetForm(forms.ModelForm, BootsTrapMixin):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth < self.MIN_DATE_OF_BIRTH or date_of_birth > self.MIN_DATE_OF_BIRTH:
            raise ValidationError(f'Date of birth must be between {self.MIN_DATE_OF_BIRTH} and {self.MAX_DATE_OF_BIRTH}')
        return date_of_birth


    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')


class DeletePetForm(forms.ModelForm, BootsTrapMixin, DisableFieldsMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['name'].required = False
        self.fields['type'].required = False
        self._init_disable_fields()

    def save(self, commit=True):
        # photos = PetPhoto.objects.filter(tagged_pet=self.instance)
        # print(photos)
        self.instance.delete()
        return self.instance

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')






