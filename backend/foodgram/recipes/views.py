import django_filters.rest_framework as django_filters
from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RecipeSubSerializer
from .filters import IngredientNameFilter, RecipeFilter
from .models import (Favorite, Ingredient, Recipe, RecipeIngredient,
                     ShoppingCart, Tag)
from .permissions import IsRecipeOwnerOrReadOnly
from .serializers import (FavoriteSerializer, IngredientSerialiser,
                          RecipeReadSerializer, RecipeWriteSerializer,
                          ShoppingCartSerializer, TagSerializer)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerialiser
    permission_classes = (AllowAny,)
    pagination_class = None
    filter_class = IngredientNameFilter


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    permission_classes = (IsRecipeOwnerOrReadOnly,)
    pagination_class = PageNumberPagination
    filter_backends = [django_filters.DjangoFilterBackend]
    filter_class = RecipeFilter

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return RecipeReadSerializer
        return RecipeWriteSerializer

    @action(
        methods=['GET', 'DELETE'],
        url_path='favorite',
        url_name='favorite',
        detail=True,
        permission_classes=(IsAuthenticated,),
    )
    def favorite(self, request, pk):
        recipe = get_object_or_404(Recipe, id=pk)
        serializer = FavoriteSerializer(
            data={'user': request.user.id, 'recipe': recipe.id}
        )
        if request.method == 'GET':
            serializer.is_valid(raise_exception=True)
            serializer.save(recipe=recipe, user=request.user)
            serializer = RecipeWriteSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        favorite = get_object_or_404(
            Favorite, user=request.user.id, recipe__id=pk
        )
        favorite.delete()
        return Response(
            f'{recipe.name} - удалено из избранного',
            status=status.HTTP_204_NO_CONTENT,
        )

    @action(
        methods=['GET'],
        detail=False,
        url_name='download_shopping_cart',
        url_path='download_shopping_cart',
        permission_classes=(IsAuthenticated,),
    )
    def download_shopping_cart(self, request):
        user = self.request.user
        recipes = user.shoppingcart.all().values_list('recipe', flat=True)
        ingredients = RecipeIngredient.objects.filter(recipe__in=recipes)
        buying_list = {}
        for ingredient in ingredients:
            name = ingredient.ingredient.name
            amount = ingredient.amount
            unit = ingredient.ingredient.measurement_unit
            if name not in buying_list:
                buying_list[name] = {'amount': amount, 'unit': unit}
            else:
                buying_list[name]['amount'] = (
                    buying_list[name]['amount'] + amount
                )
        shopping_list = []
        for item in buying_list:
            shopping_list.append(
                f'{item} - {buying_list[item]["amount"]}, '
                f'{buying_list[item]["unit"]}\n'
            )
        response = HttpResponse(shopping_list, 'Content-Type: text/plain')
        response['Content-Disposition'] = (
            'attachment;' 'filename="shopping_list.txt"'
        )
        return response


class ShoppingCartView(APIView):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'delete']

    def get(self, request, pk):
        user = request.user
        recipe = get_object_or_404(Recipe, id=pk)
        serializer = ShoppingCartSerializer(
            data={'user': user.id, 'recipe': recipe.id},
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(recipe=recipe, user=request.user)
        serializer = RecipeSubSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        user = request.user
        cart = get_object_or_404(ShoppingCart, user=user, recipe__id=pk)
        cart.delete()
        return Response(
            f'Рецепт {cart.recipe} удален из корзины',
            status=status.HTTP_204_NO_CONTENT,
        )
