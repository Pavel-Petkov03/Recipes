from django.urls import path
from Recipes.main.views.create_recipe import CreateRecipeView
from Recipes.main.views.delete_recipe import DeleteRecipeView
from Recipes.main.views.details_recipe import DetailsRecipeView
from Recipes.main.views.edit_recipe import EditRecipeView
from Recipes.main.views.home import HomeView

urlpatterns = [
    path("", HomeView.as_view()),
    path("create", CreateRecipeView.as_view()),
    path("edit/<int:pk>", EditRecipeView.as_view()),
    path("delete/<int:pk>", DeleteRecipeView.as_view()),
    path("details/<int:pk>", DetailsRecipeView.as_view()),
]
