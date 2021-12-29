from rest_framework import serializers
from .models import Favorite, Tag, Recipe, Ingredient


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(source='user.id')
    recipe = serializers.IntegerField(source='recipe.id')

    class Meta:
        model = Favorite
        fields = ('user', 'recipe')

    def validate(self, data):
        user = data['user']['id']
        recipe= data['recipe']['id']
        if Favorite.objects.filter(user=user, recipe__id=recipe).exists():
            raise serializers.ValidationError(
                {
                    "errors": "Нельзя повторно добавить в избранное"
                }
            ) 
        return data