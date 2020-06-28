from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    u_joined_at = models.DateTimeField(auto_now_add=True)
    u_phone = models.CharField(max_length=11, null=True, blank=True)
    u_email = models.CharField(max_length=30, null=True, blank=True)
    u_isAdmin = models.BooleanField(default=False)


class Excercise(models.Model):
    e_category = models.CharField(max_length=20, verbose_name="구분")
    e_name = models.CharField(max_length=20, verbose_name="이름")
    e_description = models.TextField(verbose_name="설명")
    e_recommend_count = models.IntegerField(default=0, verbose_name="인기")
    e_created_at = models.DateTimeField(auto_now_add=True)
    e_modified_at = models.DateTimeField(auto_now=True)
    e_thumbnail = models.ImageField(upload_to="exercise", blank=True, null=True, verbose_name="사진")

    def get_absolute_url(self):
        return reverse("exercise-detail", kwargs={"pk": self.pk})
    
class ToDoList(models.Model):
    tdl_title = models.CharField(max_length=20, verbose_name="제목")
    tdl_content = models.TextField(verbose_name="내용")
    tdl_date = models.DateField(verbose_name="날짜")
    tdl_created_at = models.DateTimeField(auto_now_add=True)
    tdl_modified_at = models.DateTimeField(auto_now=True)


class Magazine(models.Model):
    class meta:
        ordering = ['m_created_at']

    m_title = models.CharField(max_length=20, verbose_name="기사")
    m_content = models.TextField(verbose_name="본문")
    m_created_at = models.DateTimeField(auto_now_add=True)
    m_modified_at = models.DateTimeField(auto_now=True)
    m_thumbnail = models.ImageField(upload_to="magazine", blank=True, null=True, verbose_name="사진")

    def get_absolute_url(self):
        return reverse("magazine-detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_magazine_by_num(num):
        return Magazine.objects.all()[:num]


class Diet(models.Model):
    m_title = models.CharField(max_length=20,verbose_name="식단" )
    m_content = models.TextField(verbose_name="내용")
    m_created_at = models.DateTimeField(auto_now_add=True)
    m_modified_at = models.DateTimeField(auto_now=True)
    m_thumbnail = models.ImageField(upload_to="diet", blank=True, null=True, verbose_name="사진")
