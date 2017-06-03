# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic import ListView, DetailView, TemplateView
from recipe.models import Recipe, Foodinfo, Recipeinfo
from honeytip.models import HoneyTip, Contents
# Create your views here.

class Mypage(TemplateView) :
    template_name = 'mypage/mypage.html'

class ScrapLV(TemplateView) :
    template_name = 'mypage/mypage.html'
    

def RecipeWriteLV(request,username) :
	recipe = Recipe.objects.filter(owner = request.user.id)
	honeytip = HoneyTip.objects.filter(owner = request.user.id)
	paginate_by = 8
	return render(request, 'mypage/mypage_writelist.html', {'recipes': recipe, 'honeytips': honeytip})



    