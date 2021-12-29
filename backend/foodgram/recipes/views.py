from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Tag, Recipe, Ingredient, Favorite
from .serializers import RecipeSerializer, TagSerializer, IngredientSerialiser, FavoriteSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerialiser
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


    @action(methods=['GET', 'DELETE'], url_path='favorite', url_name='favorite', detail=True)
    def favorite(self, request, pk):
        user = request.user
        recipe = get_object_or_404(Recipe, id=pk)
        serializer = FavoriteSerializer(data={'user': user.id, 'favorited': recipe.id})
        if request.method == 'GET':
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response('Добавлено в избранное', status=status.HTTP_201_CREATED)
        favorite = get_object_or_404(Favorite, user=user.id, favorited=recipe.id)
        favorite.delete()
        return Response('Удалено из избранного', status=status.HTTP_204_NO_CONTENT)
