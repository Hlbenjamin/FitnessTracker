from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='workouts_landing'),
    path('home/', views.home, name='workouts_home'),
    path('workout/<int:workout_id>/', views.workout, name='workouts_workout'),
    path('exercise/<int:exercise_id>/', views.exercise, name='workouts_exercise'),
]
