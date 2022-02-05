from django.db import models

# Create your models here.
from django.db import models


# o	title - Character field with max length of 30 characters
# o	image_url - URL field
# o	description - Text field
# o	ingredients - Character field with max length of 250 characters
# o	time - Integer field

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(max_length=250)
    time = models.IntegerField()

    def split_ingredients(self):
        return self.ingredients.split(", ")
