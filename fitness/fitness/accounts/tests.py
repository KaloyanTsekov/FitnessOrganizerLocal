from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase as TestCase
from django.urls import reverse
from fitness.accounts.models import Profile, User

UserModel = get_user_model()


class ProfileTests(TestCase):
    VALID_PROFILE_DATA = {'first_name': 'TestFirstName', 'last_name': 'TestLastName', 'gender': 'Male', 'user_id': '1'}
    VALID_USER_DATA = {'id': '1'}
    def test_profile_create__first_name_contains_only_letters__expect_success(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create__FIRST_name_contains_letters_and_NUMBERS__expect_error(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        first_name = "TestFirstName1"
        profile = Profile(first_name=first_name,
                          last_name=self.VALID_PROFILE_DATA['last_name'],
                          gender=self.VALID_PROFILE_DATA['gender'],
                          user_id=self.VALID_PROFILE_DATA['user_id'])
        profile.save()
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)


    def test_profile_create__FIRST_name_contains_letters_and_SPECIAL_SYMBOL__expect_error(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        first_name = "TestFirstName$"
        profile = Profile(first_name=first_name,
                          last_name=self.VALID_PROFILE_DATA['last_name'],
                          gender=self.VALID_PROFILE_DATA['gender'],
                          user_id=self.VALID_PROFILE_DATA['user_id'])
        profile.save()
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)


    def test_profile_create__FIRST_name_contains_letters_and_SPACE__expect_error(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        first_name = "Test FirstName"
        profile = Profile(first_name=first_name,
                          last_name=self.VALID_PROFILE_DATA['last_name'],
                          gender=self.VALID_PROFILE_DATA['gender'],
                          user_id=self.VALID_PROFILE_DATA['user_id'])
        profile.save()
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__LAST_name_contains_letters_and_NUMBERS__expect_error(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        last_name = "TestLastName1"
        profile = Profile(first_name=self.VALID_PROFILE_DATA['first_name'],
                          last_name=last_name,
                          gender=self.VALID_PROFILE_DATA['gender'],
                          user_id=self.VALID_PROFILE_DATA['user_id'])
        profile.save()
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__LAST_name_contains_letters_and_SPECIAL_SYMBOL__expect_error(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        last_name = "TestLastName$"
        profile = Profile(first_name=self.VALID_PROFILE_DATA['first_name'],
                          last_name=last_name,
                          gender=self.VALID_PROFILE_DATA['gender'],
                          user_id=self.VALID_PROFILE_DATA['user_id'])
        profile.save()
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__LAST_name_contains_letters_and_SPACE__expect_error(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        last_name = "Test LastName"
        profile = Profile(first_name=self.VALID_PROFILE_DATA['first_name'],
                          last_name=last_name,
                          gender=self.VALID_PROFILE_DATA['gender'],
                          user_id=self.VALID_PROFILE_DATA['user_id'])
        profile.save()
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)


class ProfileViewTests(TestCase):
    VALID_PROFILE_DATA = {'first_name': 'TestFirstName', 'last_name': 'TestLastName', 'gender': 'Male', 'user_id': '1'}
    VALID_USER_DATA = {'id': '1'}

    def test_get__REGISTER__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'accounts/profile_create.html')

    def test_get__LOGIN__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'accounts/login_page.html')

    def test_get__LOGOUT_CONFIRMATION__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('logout confirmation'))
        self.assertTemplateUsed(response, 'accounts/logout_page.html')

    def test_get__EDIT_PASSWORD_SUCCESS__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('change password success'))
        self.assertTemplateUsed(response, 'accounts/successful_change_password.html')

    def test_get__DASHBOARD__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('dashboard'))
        self.assertTemplateUsed(response, 'base/dashboard.html')

    def test_get__when_two_profiles__expect_two_profiles(self):
        profiles_to_create = (
            Profile(first_name='TestFirstName', last_name='TestLastName', gender='Male', user_id=1),
            Profile(first_name='TestFirstNameTwo', last_name='TestLastNameTwo', gender='Male', user_id=2),
        )
        users_to_create = (
            User(id=1, username='UserOne'),
            User(id=2, username='UserTwo'),
        )
        User.objects.bulk_create(users_to_create)
        Profile.objects.bulk_create(profiles_to_create)
        self.assertEqual(len(Profile.objects.all()), 2)

    def test_get__create_TWO_profiles__expect_THREE_profiles__ERROR(self):
        profiles_to_create = (
            Profile(first_name='TestFirstName', last_name='TestLastName', gender='Male', user_id=1),
            Profile(first_name='TestFirstNameTwo', last_name='TestLastNameTwo', gender='Male', user_id=2),
        )
        users_to_create = (
            User(id=1, username='UserOne'),
            User(id=2, username='UserTwo'),
        )
        User.objects.bulk_create(users_to_create)
        Profile.objects.bulk_create(profiles_to_create)
        self.assertNotEqual(len(Profile.objects.all()), 3)

    def test_index_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)


















