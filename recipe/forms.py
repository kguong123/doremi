from .models import *
from django.forms.models import inlineformset_factory

RecipeinfoInlineFormSet = inlineformset_factory(Recipe, Recipeinfo,
    fields = ['image','description'],
    extra = 1)

foodinfoInlineFormSet = inlineformset_factory(Recipe, Foodinfo,
    fields = ['ingredient', 'quantity'],
    extra = 1)