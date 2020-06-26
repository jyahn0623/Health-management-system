from django.urls import path
from . import views
urlpatterns = [
    path('', views.admin_main, name="admin-main"),
    path('exercise', views.admin_exercise, name="admin-exercise"),
]