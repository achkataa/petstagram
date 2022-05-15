from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from petstagram.accounts.models import Profile
from petstagram.main.models import Pet, PetPhoto

UserModel = get_user_model()

# Create your tests here.
from django.urls import reverse


class ProfileViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'angel',
        'password': '1234Am'
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Angel',
        'last_name': 'Madin',
        'picture':'https://avatars.githubusercontent.com/u/51945879?v=4',
        'date_of_birth': date(2005, 4, 14),
    }

    def __create_valid_user_and_profile(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(**self.VALID_PROFILE_DATA, user=user)

        return (user, profile)

    def test_all_correct_should_return_the_right_template(self):
        user, profile = self.__create_valid_user_and_profile()
        response = self.client.get(reverse('profile', kwargs={'pk': profile.pk}))
        self.assertTemplateUsed('accounts/profile_details.html')

    def test_when_opening_non_existing_profile(self):
        response = self.client.get(reverse('profile', kwargs={'pk': 5}))
        self.assertEqual(404, response.status_code)

    def test_when_there_are_photos_should_return_the_right_photos_count(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)
        pet = Pet.objects.create(name='Misho', type='Cat', user=user)
        pet_photo = PetPhoto.objects.create(
            photo='asd.jpg',
            publication_date=date.today(),
            user=user,
        )
        pet_photo.tagged_pets.add(pet)
        pet_photo.save()

        response = self.client.get(reverse('profile', kwargs={'pk': profile.pk}))

        self.assertEqual(1, response.context['pets_photos_count'])

    def test_when_there_are_no_photos_should_return_zero_photos_count(self):
        pass

    def test_when_owner__is_owner__should_return_true(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.client.get(reverse('profile', kwargs={'pk': profile.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_when_not_owner__is_owner__should_return_false(self):
        user, profile = self.__create_valid_user_and_profile()
        user2 = UserModel.objects.create_user(username='gosho', password='1234GG')
        self.client.login(username='gosho', password='1234GG')

        response = self.client.get(reverse('profile', kwargs={'pk': profile.pk}))

        self.assertFalse(response.context['is_owner'])

    def test_when_no_likes_should_return_zero_likes(self):
        pass

    def test_when_likes_should_return_the_right_likes(self):
        pass

    def test_when_no_pets_should_return_zero_pets(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.client.get(reverse('profile', kwargs={'pk': profile.pk}))

        self.assertListEqual([], list(response.context['pets']))

    def test_when_pets_should_return_the_right_pets(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)
        pet = Pet.objects.create(name='Misho', type='Cat', user=user)

        response = self.client.get(reverse('profile', kwargs={'pk': profile.pk}))
        self.assertListEqual([pet], list(response.context['pets']))




