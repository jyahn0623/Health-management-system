from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from django.views.generic import View
from h_admin.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from datetime import date
import json
# 메인
def main(request):
    datas = {
        'navVisible' : False
    }
    return render(request, 'main/index.html', datas)

# 나의 운동
def excercise(request):
    m = Magazine.get_magazine_by_num(3)
    datas = {
        'current' : 'e', 
        'inner_title' : '나의 운동',
        'magazines' : m
    }
    return render(request, 'main/exercise/MyExerciseHome.html', datas)

def excercise_recommend(request):
    ex = Excercise.objects.all()
    datas = {
        'current' : 'r', 
        'inner_title' : '추천 운동',
        'ex' : ex,
    }
    return render(request, 'main/exercise/RecommendExercise.html', datas)

@csrf_exempt
def excercise_plan(request):
    f = TodoListForm()
    tdls = ToDoList.objects.all()
    if request.method == 'POST':
        tdl_title = request.POST.get('tdl_title')
        tdl_content = request.POST.get('tdl_content')
        tdl_date = request.POST.get('tdl_date')
        td = ToDoList.objects.create(
                                tdl_title=tdl_title,
                                tdl_content=tdl_content,
                                tdl_date=datetime.date.fromisoformat(tdl_date)
                            )

        td_s = serializers.serialize('json', [td], ensure_ascii=False)
        return HttpResponse(json.dumps({"msg" : "성공적으로 저장되었습니다.", "td" : td_s}), content_type='application/json')
    datas = {
        'current' : 'p', 
        'inner_title' : '운동 계획',
        'form' : f,
        'tdls' : tdls
    }
    return render(request, 'main/exercise/ExercisePlan.html', datas)

def exercise_delete(request, pk):
    pass

class ExerciseDetail(View):
    def get(self, request, pk):
        ex = get_object_or_404(Excercise, pk=pk)
        return render(request, 'main/exercise/detail.html', {
            'ex' : ex,
            'inner_title' : ex.e_name,
            'navVisible' : False
        })

class MagazineDetail(View):
    def get(self, request, pk):
        m = get_object_or_404(Magazine, pk=pk)
        return render(request, 'main/magazine/detail.html', {
            'm' : m,
            'inner_title' : m.m_title,
            'navVisible' : False
        })

# 식단
def diet(request):
    d = Diet.objects.all()
    f = DietForm()
    if request.method == 'POST':
        m_title = request.POST.get('m_title')
        m_content = request.POST.get('m_content')
        m_thumnail = request.FILES.get('m_thumbnail')
        
        Diet.objects.create(
            m_title = m_title,
            m_content = m_content,
            m_thumbnail = m_thumnail
        )
        return JsonResponse({'msg' : '성공적으로 등록되었습니다.'}, status=200)
        
    return render(request, 'main/diet/home.html', {
        'current' : 'e', 
        'form' : f,
        'diets' : d
    })

@require_http_methods(['POST'])
def diet_delete(request, pk):
    if request.method == 'POST': 
        print(pk)
        d = Diet.objects.filter(pk=pk)
        if d: d.delete()
        return JsonResponse({"msg" : "성공적으로 삭제되었습니다."}, status=200)

def getEventsByDate(request):
    print(request.GET)
    date = request.GET.get('date')
    if date:
        tds = ToDoList.objects.filter(tdl_date=date)
        sl_tds = serializers.serialize('json', tds, ensure_ascii=False)
    return JsonResponse({'tds' : sl_tds}, status=200)