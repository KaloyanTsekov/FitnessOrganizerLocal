from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase as TestCase
from django.urls import reverse

from fitness.accounts.models import User, Profile
from fitness.track.models import Results

class ResultsViewTests(TestCase):
    VALID_PROFILE_DATA = {'first_name': 'TestFirstName', 'last_name': 'TestLastName', 'gender': 'Male', 'user_id': '4'}
    VALID_USER_DATA = {'id': '4', 'username': 'User'}
    VALID_RESULT_DATA = {
        'height': 100,
        'weight': 90,
        'chest_size': 100,
        'biceps_size': 40,
        'waist_size': 90,
        'user_id': {VALID_USER_DATA['id']},
    }

    def test_get__VIEW_RESULTS__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('show result'))
        self.assertTemplateUsed(response, 'track/view_result.html')

    def test_get__ALL_FEATURES__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('results features'))
        self.assertTemplateUsed(response, 'track/all_results_features.html')

    def test_three_results_CREATED_expect_success(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()
        number_of_results = 3
        for result_id in range(number_of_results):
            result_id = Results(
                height=180,
                weight=90,
                chest_size=100,
                biceps_size=40,
                waist_size=90,
                user_id=user.id
            )
            result_id.save()
        self.assertEqual(len(Results.objects.all()), 3)

    def test_BMI_expect_success(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()
        result = Results(
            height=180,
            weight=90,
            chest_size=100,
            biceps_size=40,
            waist_size=90,
            user_id=user.id,
        )
        result.BMI = result.weight / ((result.height * result.height) / 10000)
        result.save()
        self.assertEqual(result.BMI, 27.777777777777775)

    def test_result_HEIGHT__validator_expect_ERROR(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()
        below_zero = -1
        result = Results(
            height=below_zero,
            weight=self.VALID_RESULT_DATA['weight'],
            biceps_size=self.VALID_RESULT_DATA['biceps_size'],
            chest_size=self.VALID_RESULT_DATA['chest_size'],
            waist_size=self.VALID_RESULT_DATA['waist_size'],
            user_id=self.VALID_USER_DATA['id']
        )
        result.save()
        with self.assertRaises(ValidationError) as context:
            result.full_clean()
            result.save()
        self.assertIsNotNone(context.exception)

    def test_result_WEIGHT__validator_expect_ERROR(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()
        below_zero = -1
        result = Results(
            height=self.VALID_RESULT_DATA['height'],
            weight=below_zero,
            biceps_size=self.VALID_RESULT_DATA['biceps_size'],
            chest_size=self.VALID_RESULT_DATA['chest_size'],
            waist_size=self.VALID_RESULT_DATA['waist_size'],
            user_id=self.VALID_USER_DATA['id']
        )
        result.save()
        with self.assertRaises(ValidationError) as context:
            result.full_clean()
            result.save()
        self.assertIsNotNone(context.exception)

    def test_result_BICEPS_SIZE__validator_expect_ERROR(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()
        below_zero = -1
        result = Results(
            height=self.VALID_RESULT_DATA['height'],
            weight=self.VALID_RESULT_DATA['weight'],
            biceps_size=below_zero,
            chest_size=self.VALID_RESULT_DATA['chest_size'],
            waist_size=self.VALID_RESULT_DATA['waist_size'],
            user_id=self.VALID_USER_DATA['id']
        )
        result.save()
        with self.assertRaises(ValidationError) as context:
            result.full_clean()
            result.save()
        self.assertIsNotNone(context.exception)

    def test_result_CHEST_SIZE__validator_expect_ERROR(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()
        below_zero = -1
        result = Results(
            height=self.VALID_RESULT_DATA['height'],
            weight=self.VALID_RESULT_DATA['weight'],
            biceps_size=self.VALID_RESULT_DATA['biceps_size'],
            chest_size=below_zero,
            waist_size=self.VALID_RESULT_DATA['waist_size'],
            user_id=self.VALID_USER_DATA['id']
        )
        result.save()
        with self.assertRaises(ValidationError) as context:
            result.full_clean()
            result.save()
        self.assertIsNotNone(context.exception)

    def test_result_WAIST_SIZE__validator_expect_ERROR(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()
        below_zero = -1
        result = Results(
            height=self.VALID_RESULT_DATA['height'],
            weight=self.VALID_RESULT_DATA['weight'],
            biceps_size=self.VALID_RESULT_DATA['biceps_size'],
            chest_size=self.VALID_RESULT_DATA['chest_size'],
            waist_size=below_zero,
            user_id=self.VALID_USER_DATA['id']
        )
        result.save()
        with self.assertRaises(ValidationError) as context:
            result.full_clean()
            result.save()
        self.assertIsNotNone(context.exception)

    def test_get_SHOW_RESULTS__CONTEXT__is_TRUE(self):
        UserModel = get_user_model()
        user = UserModel.objects.create_user(**{'username': 'User', 'password': '1234QRew'})
        profile = Profile.objects.create(
            **{'first_name': 'TestFirstName', 'last_name': 'TestLastName', 'gender': 'Male', 'user_id': user.id})
        self.client.login(**{'username': 'User', 'password': '1234QRew'})
        result = Results(
            height=self.VALID_RESULT_DATA['height'],
            weight=self.VALID_RESULT_DATA['weight'],
            biceps_size=self.VALID_RESULT_DATA['biceps_size'],
            chest_size=self.VALID_RESULT_DATA['chest_size'],
            waist_size=self.VALID_RESULT_DATA['waist_size'],
            user_id=1
        )
        result.save()
        response = self.client.get(reverse('edit result', kwargs={'pk': result.pk}))
        self.assertTrue(response.context['results'])
        self.assertEqual(response.status_code, 200)
