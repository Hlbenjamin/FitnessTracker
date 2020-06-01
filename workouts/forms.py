from django import forms
from .models import Exercise, Workout

class WeightForm(forms.Form):
    exercise = forms.IntegerField()
    weight = forms.DecimalField(decimal_places=0, max_digits=10000)

class WorkoutForm(forms.Form):
    workout_name = forms.CharField(max_length=100)

class ExerciseForm(forms.Form):
    workout = forms.IntegerField()
    exercise_name = forms.CharField(max_length=100)
    