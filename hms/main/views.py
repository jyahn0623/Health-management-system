from django.shortcuts import render, HttpResponse
from .models import *
# 메인
def main(request):
    return render(request, 'main/index.html')

# 나의 운동
def excercise(request):
    datas = {
        'current' : 'e', 
    }
    return render(request, 'main/exercise/MyExerciseHome.html', datas)

def excercise_recommend(request):
    ex = Excercise.objects.all()
    datas = {
        'current' : 'r', 
        'ex' : ex,
    }
    return render(request, 'main/exercise/RecommendExercise.html', datas)

def excercise_plan(request):
    datas = {
        'current' : 'p', 
    }
    return render(request, 'main/exercise/ExercisePlan.html', datas)

