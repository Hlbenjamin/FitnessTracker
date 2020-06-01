from django.shortcuts import render, redirect
from .models import Workout, Weight, Exercise, WorkoutData, ExerciseData
from .forms import WeightForm, WorkoutForm, ExerciseForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    workouts_all = WorkoutData.objects.all()
    exercise_all = ExerciseData.objects.all()
    form = ExerciseForm()
    if request.method == 'POST' and 'btnform3' in request.POST:
        form = ExerciseForm(request.POST)
        
        if form.is_valid():
            w = form.cleaned_data['workout']
            e = form.cleaned_data['exercise_name']
            new_exercise = Exercise(workout_id=w, exercise_name=e)
            new_exercise.save()

        return redirect('workouts_home')

    form = WorkoutForm()
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        
        if form.is_valid():
            w = form.cleaned_data['workout_name']
            new_workout = Workout(workout_name=w, user=request.user)
            new_workout.save()

        return redirect('workouts_home')

    context = {
        'workouts': Workout.objects.filter(user=request.user),
        'workouts_all': workouts_all,
        'exercises': exercise_all,
    }
    return render(request, 'workouts/home.html', context)



@login_required
def workout(request, workout_id):
    workouts_all = WorkoutData.objects.all()
    exercise_all = ExerciseData.objects.all()
    workout_main = Workout.objects.get(id=workout_id)
    form = WeightForm()
    if request.method == 'POST' and 'btnform1' in request.POST:
        form = WeightForm(request.POST)
        
        if form.is_valid():
            w = form.cleaned_data['weight']
            e = form.cleaned_data['exercise']
            new_weight = Weight(weight=w, exercise_id=e)
            new_weight.save()

        return redirect('workouts_workout', workout_id)

    form = ExerciseForm()
    if request.method == 'POST' and 'btnform2' in request.POST:
        form = ExerciseForm(request.POST)
        
        if form.is_valid():
            w = form.cleaned_data['workout']
            e = form.cleaned_data['exercise_name']
            new_exercise = Exercise(workout_id=w, exercise_name=e)
            new_exercise.save()

        return redirect('workouts_workout', workout_id)

    context = {
        'workout': workout_main,
        'exercises': exercise_all,
        'workouts_all': workouts_all,
        'exercises': exercise_all,
    }

    return render(request, 'workouts/workout.html', context)


@login_required
def exercise(request, exercise_id):
    exercise_main = Exercise.objects.get(id=exercise_id)
    weight_main = exercise_main.weight.all()
    context = {
        'exercise': exercise_main,
        'weights': weight_main,
    }
    return render(request, 'workouts/exercise.html', context)

def landing(request):
    return render(request, 'workouts/landing.html')



def dropdown(request):
    form = MyForm
    context = {
        'form': form,
    }
    return render(request, 'workouts/dropdown.html', context)