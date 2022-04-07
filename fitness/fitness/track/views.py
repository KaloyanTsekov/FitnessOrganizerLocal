from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from fitness.track.forms import CreateResultForm, EditResultForm
from fitness.track.models import Results


class CreateResultView(LoginRequiredMixin, views.CreateView):
    template_name = 'track/create_result.html'
    form_class = CreateResultForm
    success_url = reverse_lazy('show result')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


def get_results():
    results = Results.objects.all().order_by('date')
    if results:
        return results
    return None


def ShowResultView(request):
    all_results = get_results()
    results = []
    if all_results:
        for element in all_results:
            if element.user_id == request.user.id:
                element.BMI = f"{element.weight / ((element.height * element.height) / 10000):.2f}"
                results.append(element)

    context = {
        'results': results,
    }
    return render(request, 'track/view_result.html', context)


@login_required()
def DeleteResultView(request, pk):
    result = Results.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'result': result,
        }
        return render(request, 'track/view_result.html', context)
    else:
        result.delete()
        return redirect('show result')


@login_required()
def EditResultView(request, pk):
    results = Results.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditResultForm(request.POST, instance=results)
        if form.is_valid():
            form.save()
            return redirect('show result')

    else:
        form = EditResultForm(instance=results)
    context = {
        'form': form,
        'results': results,
    }
    return render(request, 'track/edit_result.html', context)


class AllResultsFeaturesView(views.ListView):
    model = Results
    template_name = 'track/all_results_features.html'