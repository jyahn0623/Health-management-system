from django.urls import path
from . import views
urlpatterns = [
    path('', views.admin_main, name="admin-main"),
    path('exercise', views.admin_exercise, name="admin-exercise"),
    path('exercise/<pk>/delete', views.admin_exercise_delete, name="admin-delete-exercise"),
    # path('diet', views.admin_exercise, name="admin-diet"),
    path('magazine', views.admin_magazine, name="admin-magazine"),
    path('diet', views.admin_diet, name="admin-diet"),
    path('magazine/<pk>/delete', views.admin_magazine_delete, name="admin-delete-magazine"),
    path('diet/<pk>/delete', views.admin_diet_delete, name="admin-delete-diet"),
]