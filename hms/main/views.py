from django.shortcuts import render, HttpResponse

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
    datas = {
        'current' : 'r', 
    }
    return render(request, 'main/exercise/RecommendExercise.html', datas)

def excercise_plan(request):
    datas = {
        'current' : 'p', 
    }
    return render(request, 'main/exercise/ExercisePlan.html', datas)

