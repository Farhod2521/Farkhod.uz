
from django.db import models






class Personal_Info(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Ism Familyasi")
    age  = models.IntegerField(verbose_name="Yoshi")
    Email = models.EmailField(max_length=200, verbose_name="Email")
    phone  = models.CharField(max_length=200, verbose_name="Telfon raqami")
    address = models.CharField(max_length=299, verbose_name="Manzil")
    skill = models.CharField(max_length=200, verbose_name="skill(Backend)")
    languange = models.CharField(max_length=299, verbose_name="Qaysi tillarni bilasiz")
    experience  =models.CharField(max_length=200, verbose_name="Qancha vaqtdan beri ishlaysiz")


    def __str__(self):
        return self.full_name



class MyWorkCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name="Loyiha nomi")
    link  = models.CharField(max_length=300, verbose_name="URl")
    description = models.TextField(verbose_name="Loyiha haqida")
    image =  models.ImageField(upload_to ="image")



    def __str__(self):
        return self.title


# Create your models here.
