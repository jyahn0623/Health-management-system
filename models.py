from django.db import models

# Create your models here.
class Diet(models.Model): #식단 db 
    date = models.DateField(auto_now_add=True) #날짜
    time = models.CharField(max_length=10) #date 필드에서 시간이 정해지면 알아서 아침/점심/저녁 선택
    menu = models.TextField() #메뉴 

class FoodsDiet(models.Model):
    food = models.ManyToManyField(Diet) #Diet db참조
    
