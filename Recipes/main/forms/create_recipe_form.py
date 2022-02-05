from django import forms

from Recipes.main.models import Recipe


class AddRecipeForm(forms.ModelForm):
    TITLE_MAX_LENGTH = 30
    IMAGE_URL_MAX_LENGTH = 200
    title = forms.CharField(max_length=TITLE_MAX_LENGTH, widget=forms.TextInput(attrs={
        'id': "id_title", "type": "text", "name": "title", "max_length": 30
    }))

    image_url = forms.URLField(max_length=IMAGE_URL_MAX_LENGTH, label="Image URL", widget=forms.URLInput(attrs={
        'id': "id_image_url", "type": "url", "name": "image_url", "required": True
    }))

    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={
        'id': "id_description", "type": "text", "name": "description", "required": True, "cols": 40, "rows": 10
    }))

    ingredients = forms.CharField(label="Ingredients", widget=forms.TextInput(attrs={
        'id': "id_ingredients", "type": "text", "name": "ingredients", "required": True,
    }))

    time = forms.IntegerField(label="Time (Minutes)", widget=forms.NumberInput(attrs={
        'id': "id_time", "type": "text", "name": "time"
    }))

    class Meta:
        model = Recipe
        fields = "__all__"
