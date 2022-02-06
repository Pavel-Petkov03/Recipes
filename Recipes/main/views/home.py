from django.shortcuts import render
from django.views import View

from Recipes.main.models import Recipe


class HomeView(View):
    def get(self, request):
        print(View)
        return render(request, 'index.html', {"recipes": Recipe.objects.all()})
