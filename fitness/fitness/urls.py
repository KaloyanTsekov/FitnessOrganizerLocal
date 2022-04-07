from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fitness.accounts.urls')),
    path('accounts/', include('fitness.accounts.urls')),
    path('exercises/', include('fitness.exercises.urls')),
    path('track/', include('fitness.track.urls')),
]
