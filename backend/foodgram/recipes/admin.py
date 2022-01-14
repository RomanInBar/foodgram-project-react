from django.contrib import admin
from recipes import models


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'tags__name', 'text', 'create_at')
    search_fields = ('author', 'name__startswith')
    list_filter = ('tags',)


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit')
    search_fields = ('name',)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('slug')


@admin.register(models.Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'recipe__name', 'create_at')
    search_fields = ('user__username__startswith', 'recipe__name__startswith')


@admin.register(models.ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user__username', 'recipe__name', 'create_at')
    search_fields = ('user.username__startswith', 'recipe__name__startswith')
