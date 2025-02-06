from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Comment(models.Model):
    text = models.TextField(verbose_name='Комментарий')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    publication = models.ForeignKey('webapp.Publication', on_delete=models.CASCADE, related_name='comments', verbose_name='Публикация')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')