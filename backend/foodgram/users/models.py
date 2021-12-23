from django.db import models
from django.db.models import constraints
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    email = models.EmailField(unique=True, verbose_name='Почта')
    username = models.CharField(max_length=150, unique=True, verbose_name='Логин')
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username


class Follow(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following', verbose_name='Автор')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='follower', verbose_name='Подписчики')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Подписчики'
        verbose_name_plural = 'Подписчики'
        constraints = [
            constraints.UniqueConstraint(
                fields=['author', 'user'],
                name='unique_follow'
            )
        ]

    def __str__(self) -> str:
        return f'{self.author}, {self.user}'