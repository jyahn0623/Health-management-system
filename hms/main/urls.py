from django.urls import path
from . import views
urlpatterns = [
    path("", views.main, name="main"),
    path("exercise", views.excercise, name="exercise"),
    path("exercise/recommend", views.excercise_recommend, name="exercise-recommend"),
    path("exercise/plan", views.excercise_plan, name="exercise-plan"),
]
