from django.urls import path

from fitness.track.views import CreateResultView, ShowResultView, DeleteResultView, EditResultView, \
    AllResultsFeaturesView

urlpatterns = (
    path('create/', CreateResultView.as_view(), name='create result'),
    path('show-results/', ShowResultView, name='show result'),
    path('delete/<int:pk>/', DeleteResultView, name='delete result'),
    path('edit/<int:pk>/', EditResultView, name='edit result'),
    path('all-result-features/', AllResultsFeaturesView.as_view(), name='results features'),
)


