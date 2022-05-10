from django.contrib import admin

# Register your models here.
from petstagram.main.models import Pet, PetPhoto

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass
