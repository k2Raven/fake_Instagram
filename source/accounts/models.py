from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models


class User(AbstractUser):
    email = models.EmailField(verbose_name='Почта', max_length=255, unique=True)
