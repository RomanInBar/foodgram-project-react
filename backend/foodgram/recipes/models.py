from django.core import validators
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    measurement_unit = models.CharField(max_length=10, verbose_name='Единицы измерения')

    class Meta:
        verbose_name = 'Ингрединет'
        verbose_name_plural = 'Ингрединенты'

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=256)
    color = models.CharField(max_length=150)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Слаг'
        verbose_name_plural = 'Слаг'

    def __str__(self) -> str:
        return self.slug


class Recipe(models.Model):
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient', verbose_name='Ингредиенты')
    tags =  models.ManyToManyField(Tag, verbose_name='Таг')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', verbose_name='Автор')
    image = models.ImageField()
    name =  models.CharField(max_length=256, verbose_name='Название')
    text = models.CharField(max_length=256, verbose_name='Описание')
    cooking_time = models.PositiveSmallIntegerField(validators=[MinValueValidator(1, message='Значение не может быть меньше 1')], verbose_name='Время готовки')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан', null=True)

    class Meta:
        ordering = ('name', 'author')
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self) -> str:
        return f'{self.name} - {self.author}'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredient')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe_ingredient')
    amount = models.PositiveSmallIntegerField(validators=[MinValueValidator(1, 'Минимальное значение 1')])

    class Meta:
        ordering = ('recipe',)
        verbose_name = 'Ингредиенты рецепта'
        verbose_name_plural = 'Ингредиенты рецепта'

    def __str__(self) -> str:
        return f'{self.recipe} {self.ingredient}'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favorited = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('user',)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self) -> str:
        return f'{self.user} {self.favorited}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ('user',)
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'

    def __str__(self) -> str:
        return f'{self.user} {self.shoping_cart}'
