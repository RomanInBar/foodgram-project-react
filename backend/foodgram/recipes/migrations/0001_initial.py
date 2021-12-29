# Generated by Django 4.0 on 2021-12-29 12:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранное',
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('measurement_unit', models.CharField(max_length=10, verbose_name='Единицы измерения')),
            ],
            options={
                'verbose_name': 'Ингрединет',
                'verbose_name_plural': 'Ингрединенты',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('text', models.CharField(max_length=256, verbose_name='Описание')),
                ('cooking_time', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Значение не может быть меньше 1')], verbose_name='Время готовки')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'ordering': ('name', 'author'),
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, 'Минимальное значение 1')])),
            ],
            options={
                'verbose_name': 'Ингредиенты рецепта',
                'verbose_name_plural': 'Ингредиенты рецепта',
                'ordering': ('recipe',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('color', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Слаг',
                'verbose_name_plural': 'Слаг',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
            options={
                'verbose_name': 'Список покупок',
                'verbose_name_plural': 'Список покупок',
                'ordering': ('user',),
            },
        ),
    ]
