from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from fitness.exercises.forms import CreateExerciseForm, CreateVideoForm, EditVideoForm, CreateWorkoutForm, \
    EditWorkoutForm
from fitness.exercises.models import Workout, Exercise, Video


@login_required()
def CreateExerciseView(request):
    if request.method == 'POST':
        form = CreateExerciseForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('success exercise creation') #show workout
    else:
        form = CreateExerciseForm(user=request.user)
    context = {
        'form': form,
    }
    return render(request, 'exercises/create_exercise.html', context)


class SuccessfulCreatedExerciseView(views.ListView):
    model = Exercise
    template_name = 'exercises/successful_created_exercise.html'


class CreateVideoView(LoginRequiredMixin, views.CreateView):
    template_name = 'exercises/create_videos.html'
    form_class = CreateVideoForm
    success_url = reverse_lazy('success videos creation')


class SuccessfulCreatedVideoView(views.ListView):
    model = Video
    template_name = 'exercises/successful_created_video.html'


def get_video():
    video = Video.objects.all()
    if video:
        return video
    return None


def ShowVideoView(request):  ###DONE
    video = get_video()
    context = {
        'video': video
    }
    return render(request, 'exercises/show_videos.html', context)


def ShowVideoLegsView(request):
    videos = get_video()
    video = []
    if videos:
        for element in videos:
            if element.category == 'Legs':
                video.append(element)
    context = {
        'video': video
    }
    return render(request, 'exercises/show_legs.html', context)


def ShowVideoArmsView(request):
    videos = get_video()
    video = []
    if videos:
        for element in videos:
            if element.category == 'Arms':
                video.append(element)
    context = {
        'video': video
    }
    return render(request, 'exercises/show_arms.html', context)


def ShowVideoBackView(request):
    videos = get_video()
    video = []
    if videos:
        for element in videos:
            if element.category == 'Back':
                video.append(element)
    context = {
        'video': video
    }
    return render(request, 'exercises/show_back.html', context)


def ShowVideoAbsView(request):
    videos = get_video()
    video = []
    if videos:
        for element in videos:
            if element.category == 'ABS':
                video.append(element)
    context = {
        'video': video
    }
    return render(request, 'exercises/show_abs.html', context)


def ShowVideoShouldersView(request):
    videos = get_video()
    video = []
    if videos:
        for element in videos:
            if element.category == 'Shoulders':
                video.append(element)
    context = {
        'video': video
    }
    return render(request, 'exercises/show_shoulders.html', context)


def ShowVideoChestView(request):
    videos = get_video()
    video = []
    if videos:
        for element in videos:
            if element.category == 'Chest':
                video.append(element)
    context = {
        'video': video
    }
    return render(request, 'exercises/show_chest.html', context)


def ShowVideoAllView(request):
    video = get_video()
    context = {
        'video': video
    }
    return render(request, 'exercises/show_all.html', context)


# check if the user is_staff or superuser
@login_required()
def DeleteVideoView(request, pk):
    video = Video.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'video': video,
        }

        return render(request, 'exercises/show_videos.html', context)
    else:
        video.delete()
        category_to_html = {
            'ABS': 'show abs',
            'Legs': 'show legs',
            'Arms': 'show arms',
            'Shoulders': 'show shoulders',
            'Chest': 'show chest',
            'Back': 'show back',
            'All': 'show all',
        }
        for key in category_to_html:
            if video.category == key:
                html = category_to_html[key]
                return redirect(html)


# check if the user is_staff or superuser
@login_required()
def EditVideoView(request, pk):
    video = Video.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditVideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            category_to_html = {
                'ABS': 'show abs',
                'Legs': 'show legs',
                'Arms': 'show arms',
                'Shoulders': 'show shoulders',
                'Chest': 'show chest',
                'Back': 'show back',
                'All': 'show all',
            }
            for key in category_to_html:
                if video.category == key:
                    html = category_to_html[key]
                    return redirect(html)
    else:
        form = EditVideoForm(instance=video)
    context = {
        'form': form,
        'video': video,
    }
    return render(request, 'exercises/edit_videos.html', context)


class CreateWorkoutView(LoginRequiredMixin, views.CreateView):
    template_name = 'exercises/create_workout.html'
    form_class = CreateWorkoutForm
    success_url = reverse_lazy('success workout creation')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class SuccessfulCreatedWorkoutView(views.ListView):
    model = Workout
    template_name = 'exercises/successful_created_workout.html'


def get_workout():
    workouts = Workout.objects.all()
    if workouts:
        return workouts
    return None


@login_required()
def ShowWorkoutView(request):
    all_workouts = get_workout()
    workouts = []
    if all_workouts:
        for training in all_workouts:
            if training.user_id == request.user.id:
                workouts.append(training)
    context = {
        'workouts': workouts,
    }
    return render(request, 'exercises/show_workout.html', context)


@login_required()
def EditWorkoutView(request, pk):
    workouts = Workout.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditWorkoutForm(request.POST, instance=workouts)
        if form.is_valid():
            form.save()
            return redirect('show workout')
    else:
        form = EditWorkoutForm(instance=workouts)
    context = {
        'form': form,
        'workouts': workouts,
    }
    return render(request, 'exercises/edit_workout.html', context)


@login_required()
def DeleteWorkoutView(request, pk):
    workout = Workout.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'workout': workout,
        }
        return render(request, 'exercises/show_workout.html', context)
    else:
        workout.delete()
        return redirect('show workout')


@login_required()
def ExerciseView(request, training_id):
    workout = Workout.objects.get(id=training_id)
    exercises = Exercise.objects.filter(training__id=training_id)
    return render(
        request,
        'exercises/exercise.html',
        {'workout': workout, 'exercises': exercises}
    )

class AllWorkoutFeaturesView(views.ListView):
    model = Workout
    template_name = 'exercises/all_workout_features.html'