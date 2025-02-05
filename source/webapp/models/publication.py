from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Publication(models.Model):
    picture = models.ImageField(upload_to='publications', verbose_name="Картинка")
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(User, related_name='publications', on_delete=models.CASCADE, verbose_name='Автор')
    likes_counter = models.PositiveIntegerField(default=0, verbose_name='Счетчик лайков')
    comments_counter = models.PositiveIntegerField(default=0, verbose_name='Счетчик комментариев')

