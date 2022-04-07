from django.contrib.auth import views as auth_view
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic as views
from django.urls import reverse_lazy
from fitness.accounts.forms import CreateProfileForm, DeleteProfileForm
from fitness.accounts.models import Profile, User
from fitness.common.view_mixins import RedirectToDashboard


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')

    # def form_valid helps to log in automatically after registration
    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


class UserLoginView(auth_view.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ChangeUserPasswordView(auth_view.PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('change password success')


class SuccessfulPasswordChangeView(views.ListView):
    model = Profile
    template_name = 'accounts/successful_change_password.html'


class UserLogoutView(auth_view.LogoutView):
    template_name = 'base/base.html'


class UserLogoutConfirmationView(views.ListView):
    model = Profile
    template_name = 'accounts/logout_page.html'


class DeleteUserProfileView(LoginRequiredMixin, views.DeleteView):
    model = User
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('dashboard')
    form_class = DeleteProfileForm


class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'base/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context

class DashboardView(views.ListView):
    model = Profile
    template_name = 'base/dashboard.html'

class AllProfileFeaturesView(views.ListView):
    model = Profile
    template_name = 'accounts/all_profile_features.html'

class AllAdminFeaturesView(views.ListView):
    model = Profile
    template_name = 'accounts/all_admin_features.html'