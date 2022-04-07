from django import forms
from fitness.common.helpers import BootstrapFormMixin
from fitness.exercises.models import Exercise, Video, Workout


class CreateExerciseForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('name', 'weight', 'series', 'reps', 'training')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['training'].queryset = Workout.objects.filter(user=user)


class CreateVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('name', 'category', 'youtube_link')


class DeleteVideoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Video
        fields = ('name', 'category', 'youtube_link')


class EditVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('name', 'category', 'youtube_link')


class CreateWorkoutForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        results = super().save(commit=False)
        results.user = self.user
        if commit:
            results.save()
        return results

    class Meta:
        model = Workout
        fields = ('name', 'day', 'category')


class EditWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('name', 'day', 'category')
