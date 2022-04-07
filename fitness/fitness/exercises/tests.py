from django.contrib.auth import get_user_model
from django.test import TestCase as TestCase
from django.urls import reverse
from fitness.accounts.models import User, Profile
from fitness.exercises.models import Workout, Video, Exercise
from fitness.exercises.views import get_video


class VideoTest(TestCase):
    UserModel = get_user_model()
    VALID_PROFILE_DATA = {'first_name': 'TestFirstName', 'last_name': 'TestLastName', 'gender': 'Male', 'user_id': '4'}
    VALID_USER_DATA = {'id': '4', 'username': 'User'}

    def test_get__SHOW_VIDEOS__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('show videos'))
        self.assertTemplateUsed(response, 'exercises/show_videos.html')

    def test_get__SHOW_VIDEO_CREATION__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('success videos creation'))
        self.assertTemplateUsed(response, 'exercises/successful_created_video.html')

    def test_get__SHOW_ABS__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('show abs'))
        self.assertTemplateUsed(response, 'exercises/show_abs.html')

    def test_get__SHOW_ARMS__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('show arms'))
        self.assertTemplateUsed(response, 'exercises/show_arms.html')

    def test_get__SHOW_BACK__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('show back'))
        self.assertTemplateUsed(response, 'exercises/show_back.html')

    def test_get__SHOW_CHEST__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('show chest'))
        self.assertTemplateUsed(response, 'exercises/show_chest.html')

    def test_get__SHOW_LEGS__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('show legs'))
        self.assertTemplateUsed(response, 'exercises/show_legs.html')

    def test_get__SHOW_SHOULDERS__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('show shoulders'))
        self.assertTemplateUsed(response, 'exercises/show_shoulders.html')

    def test_get__SHOW_ALL_EXERCISES__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('show all'))
        self.assertTemplateUsed(response, 'exercises/show_all.html')

    def test_filter_get_ARMS_VIDEO_expect_success(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()
        video_chest = Video(name='ChestWorkout', youtube_link='https://www.youtube.com/embed/bgu7QzDihzo', category='Chest')
        video_back = Video(name='BackWorkout', youtube_link='https://www.youtube.com/embed/bgu7QzDihzo', category='Back')
        video_arms = Video(name='ArmsWorkout', youtube_link='https://www.youtube.com/embed/bgu7QzDihzo', category='Arms')
        video_chest.save()
        video_back.save()
        video_arms.save()

        output = get_video()
        video = []
        if output:
            for element in output:
                if element.category == 'Arms':
                    video.append(element)

        self.assertEqual(*video, video_arms)

    def test_filter_get_BACK_VIDEO_expect_success(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()

        video_chest = Video(name='ChestWorkout', youtube_link='https://www.youtube.com/embed/bgu7QzDihzo', category='Chest')
        video_back = Video(name='BackWorkout', youtube_link='https://www.youtube.com/embed/bgu7QzDihzo', category='Back')
        video_arms = Video(name='ArmsWorkout', youtube_link='https://www.youtube.com/embed/bgu7QzDihzo', category='Arms')
        video_chest.save()
        video_back.save()
        video_arms.save()
        output = get_video()
        video = []
        if output:
            for element in output:
                if element.category == 'Back':
                    video.append(element)
        self.assertEqual(*video, video_back)

    def test_filter_get_CHEST_VIDEO_expect_success(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()

        video_chest = Video(name='ChestWorkout', youtube_link='https://www.youtube.com/embed/bgu7QzDihzo', category='Chest')
        video_back = Video(name='BackWorkout', youtube_link='https://www.youtube.com/embed/bgu7QzDihzo', category='Back')
        video_arms = Video(name='ArmsWorkout', youtube_link='https://www.youtube.com/embed/bgu7QzDihzo', category='Arms')
        video_chest.save()
        video_back.save()
        video_arms.save()
        output = get_video()
        video = []
        if output:
            for element in output:
                if element.category == 'Chest':
                    video.append(element)
        self.assertEqual(*video, video_chest)

    def test_DELETE_VIDEO__CONTEXT_is_TRUE(self):

        user = self.UserModel.objects.create_user(**{'username': 'User', 'password': '1234QRew'})
        Profile.objects.create(
            **{'first_name': 'TestFirstName', 'last_name': 'TestLastName', 'gender': 'Male', 'user_id': user.id})
        video_chest = Video(name='ChestWorkout', youtube_link='https://www.youtube.com/embed/bgu7QzDihzo',
                            category='Chest')
        video_chest.save()

        self.client.login(**{'username': 'User', 'password': '1234QRew'})
        response = self.client.get(reverse('delete videos', kwargs={'pk': video_chest.pk}))
        self.assertTrue(response.context['video'])


class WorkoutTest(TestCase):
    UserModel = get_user_model()
    VALID_PROFILE_DATA = {'first_name': 'TestFirstName', 'last_name': 'TestLastName', 'gender': 'Male', 'user_id': '4'}
    VALID_USER_DATA = {'id': '4', 'username': 'User'}

    def test_get__SHOW_VIDEO__TEMPLATE__expect_success(self):
        response = self.client.get(reverse('workout features'))
        self.assertTemplateUsed(response, 'exercises/all_workout_features.html')

    def test_filter_get_CHEST_WORKOUT_expect_success(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()

        workout_chest = Workout(name='ChestWorkout',category='Chest', day='Monday', user_id=user.id)
        workout_back = Workout(name='BackWorkout', category='Back', day='Monday', user_id=user.id)
        workout_arms = Workout(name='ArmsWorkout', category='Arms', day='Monday', user_id=user.id)
        workout_chest.save()
        workout_back.save()
        workout_arms.save()

        output = Workout.objects.all().filter(category='Chest')[0]
        self.assertEqual(output, workout_chest)

    def test_filter_get_BACK_WORKOUT_expect_success(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()

        workout_chest = Workout(name='ChestWorkout',category='Chest', day='Monday', user_id=user.id)
        workout_back = Workout(name='BackWorkout', category='Back', day='Monday', user_id=user.id)
        workout_arms = Workout(name='ArmsWorkout', category='Arms', day='Monday', user_id=user.id)
        workout_chest.save()
        workout_back.save()
        workout_arms.save()

        output = Workout.objects.all().filter(category='Back')[0]
        self.assertEqual(output, workout_back)

    def test_filter_get_ARMS_WORKOUT_expect_success(self):
        user = User(**self.VALID_USER_DATA)
        user.save()
        profile = Profile(**self.VALID_PROFILE_DATA)
        profile.save()

        workout_chest = Workout(name='ChestWorkout', category='Chest', day='Monday', user_id=user.id)
        workout_back = Workout(name='BackWorkout', category='Back', day='Monday', user_id=user.id)
        workout_arms = Workout(name='ArmsWorkout', category='Arms', day='Monday', user_id=user.id)
        workout_chest.save()
        workout_back.save()
        workout_arms.save()

        output = Workout.objects.all().filter(category='Arms')[0]
        self.assertEqual(output, workout_arms)

    def test_EDIT_workout__CONTEXT_is_TRUE(self):
        user = self.UserModel.objects.create_user(**{'username': 'User', 'password':'1234QRew'})
        Profile.objects.create(**{'first_name': 'TestFirstName', 'last_name': 'TestLastName', 'gender': 'Male', 'user_id': user.id})
        workout_chest = Workout(name='ChestWorkout', category='Chest', day='Monday', user_id=user.id)
        workout_chest.save()

        self.client.login(**{'username': 'User', 'password': '1234QRew'})
        response = self.client.get(reverse('edit workout', kwargs={'pk': workout_chest.id}))
        self.assertTrue(response.context['workouts'])

    def test_DELETE_workout__CONTEXT_is_TRUE(self):
        user = self.UserModel.objects.create_user(**{'username': 'User', 'password':'1234QRew'} )
        Profile.objects.create(**{'first_name': 'TestFirstName', 'last_name': 'TestLastName', 'gender': 'Male', 'user_id': user.id})
        workout_chest = Workout(name='ChestWorkout', category='Chest', day='Monday', user_id=user.id)
        workout_chest.save()

        self.client.login(**{'username': 'User', 'password': '1234QRew'})
        response = self.client.get(reverse('delete workout', kwargs={'pk': workout_chest.pk}))
        self.assertTrue(response.context['workout'])


    def test_SHOW_workout__CONTEXT_is_TRUE(self):
        user = self.UserModel.objects.create_user(**{'username': 'User', 'password': '1234QRew'} )
        Profile.objects.create(**{'first_name': 'TestFirstName', 'last_name': 'TestLastName', 'gender': 'Male', 'user_id': user.id})
        workout_chest = Workout(name='ChestWorkout', category='Chest', day='Monday', user_id=user.id)
        workout_chest.save()

        self.client.login(**{'username': 'User', 'password': '1234QRew'})
        response = self.client.get(reverse('show workout'))
        self.assertTrue(response.context['workouts'])

class ExerciseTest(TestCase):
    UserModel = get_user_model()

    def test_get__CREATE_EXERCISES__CONTEXT__is_TRUE(self):
        user = self.UserModel.objects.create_user(**{'username': 'User', 'password': '1234QRew'} )
        Profile.objects.create(**{'first_name': 'TestFirstName', 'last_name': 'TestLastName', 'gender': 'Male', 'user_id': user.id})
        workout_chest = Workout(name='ChestWorkout', category='Chest', day='Monday', user_id=user.id)
        workout_chest.save()
        exercise = Exercise(name='ExerciseName', weight='100', series='10', reps='10', training_id=workout_chest.id)
        exercise.save()

        self.client.login(**{'username': 'User', 'password': '1234QRew'})
        response = self.client.get(reverse('create exercise'))
        self.assertTrue(response.context['form'])
