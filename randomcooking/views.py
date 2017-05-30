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
from recipe.models import Recipe, Foodinfo, Recipeinfo

# Create your views here.


class randomcooking(TemplateView) :
    template_name = 'templates/randomcooking.html'

class random(ListView) :
    template_name = 'templates/randomcooking_all.html'
    context_object_name='recipes' 

    def get_queryset(self):
   		return Recipe.objects.order_by('?')[:1]