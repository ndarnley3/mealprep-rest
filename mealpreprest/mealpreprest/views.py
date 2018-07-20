from django.shortcuts import render

from rest_framework import viewsets

from mealpreprest.mealpreprest.models import Recipe
from mealpreprest.mealpreprest.serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited
    """

    queryset = Recipe.objects.all().order_by('-id')
    serializer_class = RecipeSerializer