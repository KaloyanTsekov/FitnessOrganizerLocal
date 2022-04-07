from django.urls import path

from fitness.exercises.views import CreateVideoView, SuccessfulCreatedVideoView, EditVideoView, DeleteVideoView, \
    ShowVideoView, ShowVideoAllView, ShowVideoAbsView, ShowVideoArmsView, ShowVideoBackView, ShowVideoChestView, \
    ShowVideoLegsView, ShowVideoShouldersView, SuccessfulCreatedWorkoutView, CreateWorkoutView, \
    EditWorkoutView, DeleteWorkoutView, ShowWorkoutView, SuccessfulCreatedExerciseView, CreateExerciseView, \
    ExerciseView, AllWorkoutFeaturesView

urlpatterns = (
    path('create-videos/', CreateVideoView.as_view(), name='create videos'),
    path('success-video-creation/', SuccessfulCreatedVideoView.as_view(), name='success videos creation'),
    path('edit-videos/<int:pk>/', EditVideoView, name='edit videos'),
    path('delete-videos/<int:pk>/', DeleteVideoView, name='delete videos'),
    path('show-videos/', ShowVideoView, name='show videos'),
    path('all-workout-features/', AllWorkoutFeaturesView.as_view(), name='workout features'),

    path('videos/all/', ShowVideoAllView, name='show all'),
    path('videos/abs/', ShowVideoAbsView, name='show abs'),
    path('videos/arms/', ShowVideoArmsView, name='show arms'),
    path('videos/back/', ShowVideoBackView, name='show back'),
    path('videos/chest/', ShowVideoChestView, name='show chest'),
    path('videos/legs/', ShowVideoLegsView, name='show legs'),
    path('videos/shoulders/', ShowVideoShouldersView, name='show shoulders'),

    path('create-workout/', CreateWorkoutView.as_view(), name='create workout'),  #Training predi
    path('success-workout-creation/', SuccessfulCreatedWorkoutView.as_view(), name='success workout creation'),
    path('edit-workout/<int:pk>/', EditWorkoutView, name='edit workout'),
    path('delete-workout/<int:pk>/', DeleteWorkoutView, name='delete workout'),
    path('show-workout/', ShowWorkoutView, name='show workout'),


    path('exercise/<int:training_id>/', ExerciseView, name='exercise'),
    path('create-exercise/', CreateExerciseView, name='create exercise'),
    path('success-exercise-creation/', SuccessfulCreatedExerciseView.as_view(), name='success exercise creation'),
)