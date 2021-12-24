# Generated by Django 4.0 on 2021-12-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_follow_author_alter_follow_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=150, unique=True, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Создан'),
        ),
    ]