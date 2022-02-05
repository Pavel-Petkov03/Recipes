from django.shortcuts import render
from django.views import View


class CreateRecipeView(View):
    def get(self, request):
        return render(request, 'create.html')
