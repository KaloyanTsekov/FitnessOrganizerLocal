from django import forms
from fitness.common.helpers import BootstrapFormMixin
from fitness.track.models import Results


class CreateResultForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        results = super().save(commit=False)
        results.user = self.user
        if commit:
            results.save()

        return results

    class Meta:
        model = Results
        fields = ('height', 'weight', 'biceps_size', 'chest_size', 'waist_size')


class EditResultForm(forms.ModelForm):
    class Meta:
        model = Results
        fields = ('height', 'weight', 'biceps_size', 'chest_size', 'waist_size')
