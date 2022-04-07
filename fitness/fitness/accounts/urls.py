from django.urls import path

from fitness.accounts.views import UserLoginView, UserRegisterView, ChangeUserPasswordView, \
    SuccessfulPasswordChangeView, UserLogoutView, UserLogoutConfirmationView, DeleteUserProfileView, DashboardView, \
    HomeView, AllProfileFeaturesView, AllAdminFeaturesView

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('logout-confirmation/', UserLogoutConfirmationView.as_view(), name='logout confirmation'),

    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('success-password-change/', SuccessfulPasswordChangeView.as_view(), name='change password success'),
    path('delete/<int:pk>/', DeleteUserProfileView.as_view(), name='delete profile'),
    path('all-profile-features/', AllProfileFeaturesView.as_view(), name='profile features'),
    path('all-admin-features/', AllAdminFeaturesView.as_view(), name='admin features'),
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
)