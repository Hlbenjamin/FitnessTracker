from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class WorkoutData(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    @property
    def exercise(self):
        return self.workout_data.all()
class ExerciseData(models.Model):
    workout_data = models.ForeignKey(WorkoutData, on_delete=models.CASCADE, related_name='workout_data')
    name = models.CharField(max_length=100)
    image = models.ImageField(default='exercise.jpg', upload_to='exercise_pics')
    def __str__(self):
        return self.name



class Workout(models.Model):
    workout_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.workout_name
    @property
    def exercise(self):
        return self.workout.all()



class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='workout')
    exercise_name = models.CharField(max_length=100)
    image = models.ImageField(default='exercise.jpg', upload_to='exercise_pics')

    def __str__(self):
        return self.exercise_name
    @property
    def weight(self):
        return self.exercise.all()



class Weight(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='exercise')
    weight = models.DecimalField(decimal_places=0, max_digits=10000)
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.weight}'


