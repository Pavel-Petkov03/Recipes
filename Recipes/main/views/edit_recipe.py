from django.shortcuts import render, redirect
from django.views import View

from Recipes.main.forms.create_recipe_form import AddRecipeForm
from Recipes.main.models import Recipe


class EditRecipeView(View):
    def get(self, request, pk):
        current_receipt = Recipe.objects.get(id=pk)
        form = AddRecipeForm(instance=current_receipt)
        return render(request, 'edit.html', {"form": form})

    def post(self, request, pk):
        current_receipt = Recipe.objects.get(id=pk)
        form = AddRecipeForm(request.POST, instance=current_receipt)
        form.save()
        return redirect("/")
