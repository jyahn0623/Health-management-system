from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .forms import *
from main.models import *

def admin_main(request):
    return render(request, 'h_admin/index.html', {
        
    })

def admin_exercise(request):
    o = None
    if request.GET.get('pk'):
        try:
            o = Excercise.objects.get(pk=request.GET.get('pk'))
        except:
            return redirect('/manage/exercise')

        e_forms = ExerciseForm(instance=o)
    else:
        e_forms = ExerciseForm()

    ex = Excercise.objects.all()
    if request.method == 'POST':    
        e_forms = ExerciseForm(request.POST, request.FILES, instance= o if o else None )
        if e_forms.is_valid():
            form = e_forms.save(commit=False)
            form.save()
            messages.success(request, '운동이 등록되었습니다.')
            return redirect('/manage/exercise')
        else:
            f = ExerciseForm(request.POST)
            return render(request, 'h_admin/index.html',  {
                'e_forms' : f,
            })


    return render(request, 'h_admin/exercise.html', {
        'ex' : ex,
        'e_forms' : e_forms,
    })

def admin_magazine(request):
    o = None
    if request.GET.get('pk'):
        try:
            o = Magazine.objects.get(pk=request.GET.get('pk'))
        except:
            return redirect('/manage/magazine')

        e_forms = MagazineForm(instance=o)
    else:
        e_forms = MagazineForm()
    ex = Magazine.objects.all()
    if request.method == 'POST':    
        e_forms = MagazineForm(request.POST, request.FILES, instance= o if o else None )
        if e_forms.is_valid():
            form = e_forms.save(commit=False)
            form.save()
            messages.success(request, '매거진이 등록되었습니다.')
            return redirect('/manage/magazine')
        else:
            f = MagazineForm(request.POST)
            return render(request, 'h_admin/index.html',  {
                'e_forms' : f,
            })


    return render(request, 'h_admin/magazine.html', {
        'ex' : ex,
        'e_forms' : e_forms,
    })


def admin_diet(request):
    o = None
    if request.GET.get('pk'):
        try:
            o = Diet.objects.get(pk=request.GET.get('pk'))
        except:
            return redirect('/manage/diet')

        e_forms = DietForm(instance=o)
    else:
        e_forms = DietForm()

    ex = Diet.objects.all()
    if request.method == 'POST':    
        e_forms = DietForm(request.POST, request.FILES, instance= o if o else None )
        if e_forms.is_valid():
            form = e_forms.save(commit=False)
            form.save()
            messages.success(request, '식단이 등록되었습니다.')
            return redirect('/manage/diet')
        else:
            f = DietForm(request.POST)
            return render(request, 'h_admin/index.html',  {
                'e_forms' : f,
            })


    return render(request, 'h_admin/diet.html', {
        'ex' : ex,
        'e_forms' : e_forms,
    })

def admin_exercise_delete(request, pk):
    o = Excercise.objects.filter(pk=pk)
    if o: o.delete()
    return JsonResponse({'msg' : '삭제가 완료되었습니다.'}, status=200)


def admin_magazine_delete(request, pk):
    o = Magazine.objects.filter(pk=pk)
    if o: o.delete()
    return JsonResponse({'msg' : '삭제가 완료되었습니다.'}, status=200)


def admin_diet_delete(request, pk):
    o = Diet.objects.filter(pk=pk)
    if o: o.delete()
    return JsonResponse({'msg' : '삭제가 완료되었습니다.'}, status=200)
