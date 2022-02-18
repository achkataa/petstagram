from django import forms

from petstagram.main.helpers import BootsTrapMixin
from petstagram.main.models import Profile, PetPhoto, Pet


class CreateProfileForm(BootsTrapMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'picture': forms.TextInput(attrs={'placeholder': 'Enter URL'})
        }

class EditProfileForm(CreateProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'description': forms.Textarea(attrs={'placeholder': ' Enter description', 'rows': 3}),
            'date_of_birth': forms.DateInput(attrs={'min': '1920-01-01'})
        }


class DeleteProfile(forms.ModelForm):

    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
