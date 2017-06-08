from .models import *
from django.forms.models import inlineformset_factory
from django.forms import ModelForm, Textarea
from django import forms

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','foodname', 'titleimage', 'servings','cookingtime']

class RecipeinfoForm(ModelForm):
    class Meta:
        model = Recipeinfo
        widgets = {
          'description': Textarea(attrs={'rows':200, 'cols':20}),
        }
        fields = ['image', 'description']

RecipeinfoInlineFormSet = inlineformset_factory(Recipe, Recipeinfo,
    fields = ['image','description'],
    extra = 2)

foodinfoInlineFormSet = inlineformset_factory(Recipe, Foodinfo,
    fields = ['ingredient', 'quantity'],
    extra = 2)



