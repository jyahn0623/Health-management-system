from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.main, name="main"),
    path("exercise", views.excercise, name="exercise"),
    path("exercise/recommend", views.excercise_recommend, name="exercise-recommend"),
    path("exercise/plan", views.excercise_plan, name="exercise-plan"),
    path("exercise/<pk>", views.ExerciseDetail.as_view(), name="exercise-detail"),
    path("exercise/<pk>/delete", views.exercise_delete, name="exercise-delete"),
    path("magazine/<pk>", views.MagazineDetail.as_view(), name="magazine-detail"),
    path("diet", views.diet, name="diet"),
    path("diet/<pk>/delete", views.diet_delete, name="diet-delete"),
    path("rest/tdl", views.getEventsByDate, name="rest-get-tdl")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



