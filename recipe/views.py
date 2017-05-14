# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from django.views.generic.edit import FormView
from django.db.models import Q

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from DjangoApp.views import LoginRequiredMixin
from django.shortcuts import redirect
from .forms import RecipeinfoInlineFormSet, foodinfoInlineFormSet
from .models import *


# Create your views here.


class RecipeLV(ListView) :
    model = Recipe
    template_name = 'recipe/recipe_all.html'
    context_object_name = 'recipes'
    paginate_by = 8

class RecipeDV(DetailView) :
    model = Recipe

class RecipeCreateView(ListView):
    model = Recipe
    template_name = 'recipe/recipe_form.html'


class RecipeCV(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['title', 'slug', 'foodname', 'titleimage', 'servings','cookingtime','viewcount','scraps', 'owner']
    template_name = 'recipe/recipe_form.html'

    def get_context_data(self, **kwargs):
        context = super(RecipeCV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = foodinfoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = foodinfoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('recipe/recipe_all.html', pk=self.object.id)
        else:
            return self.render_to_response(self.get_context_data(form=form))
