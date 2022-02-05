from django.shortcuts import redirect, render
from django.views import View

from Recipes.main.forms.create_recipe_form import AddRecipeForm
from Recipes.main.models import Recipe


class DeleteRecipeView(View):
    def get(self, request, pk):
        current_recipe = Recipe.objects.get(id=pk)
        form = AddRecipeForm(instance=current_recipe)
        form.disable_fields()
        return render(request, 'delete.html', {"form": form})

    def post(self, req, pk):
        Recipe.objects.get(id=pk).delete()
        return redirect("/")
