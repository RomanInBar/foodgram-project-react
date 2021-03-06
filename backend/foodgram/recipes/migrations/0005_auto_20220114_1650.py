# Generated by Django 3.2.5 on 2022-01-14 16:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0004_alter_recipeingredient_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={
                'ordering': ('name',),
                'verbose_name': 'Ингрединет',
                'verbose_name_plural': 'Ингрединенты',
            },
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={
                'ordering': ('-create_at',),
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.AlterField(
            model_name='favorite',
            name='recipe',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='in_favorite',
                to='recipes.recipe',
                verbose_name='Рецепт',
            ),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name='Пользователь',
            ),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='recipe_ingredient',
                to='recipes.ingredient',
                verbose_name='Ингредиент',
            ),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='recipe_ingredient',
                to='recipes.recipe',
                verbose_name='Рецепт',
            ),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='recipe',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='recipes.recipe',
                verbose_name='Рецепт',
            ),
        ),
        migrations.AlterField(
            model_name='shoppingcart',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='shoppingcart',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Пользователь',
            ),
        ),
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=150, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(
                max_length=200, unique=True, verbose_name='Слаг'
            ),
        ),
        migrations.AddConstraint(
            model_name='favorite',
            constraint=models.UniqueConstraint(
                fields=('user', 'recipe'), name='unique_favorites'
            ),
        ),
        migrations.AddConstraint(
            model_name='shoppingcart',
            constraint=models.UniqueConstraint(
                fields=('user', 'recipe'), name='unique_shopping_cart'
            ),
        ),
    ]
