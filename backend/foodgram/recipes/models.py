from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    measurement_unit = models.CharField(max_length=10)


class Tag(models.Model):
    name = models.CharField(max_length=256)
    color = models.CharField(max_length=150)
    slug = models.SlugField()


class Recipe(models.Model):
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    tags =  models.ForeignKey(Tag, on_delete=models.CASCADE)
    image = models.ImageField()
    name =  models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    cooking_time = models.PositiveSmallIntegerField()
