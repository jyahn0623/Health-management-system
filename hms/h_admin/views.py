from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from main.models import *

def admin_main(request):
    return render(request, 'h_admin/index.html', {
    })

def admin_exercise(request):
    ex = Excercise.objects.all()
    e_forms = ExerciseForm()
    if request.method == 'POST':    
        e_forms = ExerciseForm(request.POST)
        if e_forms.is_valid():
            form = e_forms.save(commit=False)
            # form.ib_user = ib_user
            form.save()
            messages.success(request, '운동이 등록되었습니다.')
            return redirect('/manage')
        else:
            print(e_forms.has_error())
            f = ExerciseForm(request.POST)
            return render(request, 'h_admin/index.html',  {
                'e_forms' : f,
            })


    return render(request, 'h_admin/exercise.html', {
        'ex' : ex,
        'e_forms' : e_forms,
    })

