from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from fitness.accounts.models import Profile, User
from fitness.exercises.models import Video, Workout
from fitness.track.models import Results


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def username(self, obj):
        return obj.user.username


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'is_superuser')

    def username(self, obj):
        return obj.user.username
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    pass

@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    pass



