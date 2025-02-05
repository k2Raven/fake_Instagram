from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

GENDER_CHOICES = (
    ('man', 'Мужчина'),
    ('woman', 'Женщина'),
)

class User(AbstractUser):
    email = models.EmailField(verbose_name='Почта', max_length=255, unique=True)
    avatar = models.ImageField(upload_to='avatars', verbose_name='Аватарка')
    user_info = models.TextField(null=True, blank=True, verbose_name='Информация о пользователе')
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Номер телефона')
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES, verbose_name="Пол")
    count_publications = models.IntegerField(default=0, verbose_name='Количество публикаций')
