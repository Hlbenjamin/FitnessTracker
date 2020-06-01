from django.contrib import admin
from .models import Workout, Exercise, Weight, WorkoutData, ExerciseData

# Register your models here.
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(Weight)
admin.site.register(WorkoutData)
admin.site.register(ExerciseData)