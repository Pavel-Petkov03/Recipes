from django.shortcuts import render, redirect
from django.views import View

from Recipes.main.forms.create_recipe_form import AddRecipeForm


class CreateRecipeView(View):
    def get(self, request):
        return render(request, 'create.html', {"form": AddRecipeForm()})

    def post(self, request):
        add_form = AddRecipeForm(request.POST)
        add_form.save()
        return redirect("/")
