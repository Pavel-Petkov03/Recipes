from django.shortcuts import render
from django.views import View

from Recipes.main.models import Recipe


class DetailsRecipeView(View):
    def get(self, request, pk):
        current_recipe = Recipe.objects.get(id=pk)
        return render(request, 'details.html', {"recipe": current_recipe})
