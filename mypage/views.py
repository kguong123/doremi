# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from django.views.generic import ListView, DetailView, TemplateView
from recipe.models import Recipe, Foodinfo, Recipeinfo
from honeytip.models import HoneyTip, Contents
from .models import RecipeScrap, HoneyTipScrap
from django.db.models import F
import operator
from django.db.models import Q

# Create your views here.

class Mypage(TemplateView) :
    template_name = 'mypage/mypage.html'

def WriteLV(request,username) :
	recipe = Recipe.objects.filter(owner = request.user.id)
	honeytip = HoneyTip.objects.filter(owner = request.user.id)
	paginate_by = 8
	return render(request, 'mypage/mypage_writelist.html', {'recipes': recipe, 'honeytips': honeytip})


def ScrapLV(request,username) :
	recipe_slug_list = RecipeScrap.objects.filter(user = request.user.id)
	rcount =0
	for i in recipe_slug_list:
		rcount = rcount+1
	honytip_slug_list = HoneyTipScrap.objects.filter(user = request.user.id)
	hcount =0
	for i in honytip_slug_list:
		hcount = hcount+1
	
	if (rcount==0 and hcount==0):
		return render(request, 'mypage/mypage_scraplist.html', {})
	elif(rcount ==0 or hcount==0):
		if (rcount==0):
			query = reduce(operator.or_, (Q(slug__contains = scrap.slug) for scrap in honytip_slug_list))
			honeytip = HoneyTip.objects.filter(query)
			return render(request, 'mypage/mypage_scraplist.html', {'honeytips': honeytip})
		elif(hcount ==0):
			query = reduce(operator.or_, (Q(slug__contains = scrap.slug) for scrap in recipe_slug_list))
			recipe = Recipe.objects.filter(query)
			return render(request, 'mypage/mypage_scraplist.html', {'recipes': recipe})
	elif (rcount!=0 and hcount!=0):
		query = reduce(operator.or_, (Q(slug__contains = scrap.slug) for scrap in honytip_slug_list))
		honeytip = HoneyTip.objects.filter(query)
		query = reduce(operator.or_, (Q(slug__contains = scrap.slug) for scrap in recipe_slug_list))
		recipe = Recipe.objects.filter(query)
		return render(request, 'mypage/mypage_scraplist.html', {'recipes': recipe, 'honeytips': honeytip})
	
def RecipeSV(request, slug) :
	ck = RecipeScrap.objects.filter(slug = slug, user=request.user.id)
	count=0
	for i in ck:
		count=count+1
	if(count == 0):
		p = RecipeScrap(slug = slug, user=request.user.id)
		p.save()
		Recipe.objects.filter(slug=slug).update(scraps=F('scraps') + 1)
	else:
		fb = RecipeScrap.objects.get(slug=slug, user=request.user.id)
		fb.delete()
		Recipe.objects.filter(slug=slug).update(scraps=F('scraps') - 1)
	return redirect(request.META['HTTP_REFERER'])


def HoneyTipSV(request,slug) :
	ck = HoneyTipScrap.objects.filter(slug = slug, user=request.user.id)
	count=0
	for i in ck:
		count=count+1
	if(count == 0):
		p = HoneyTipScrap(slug = slug, user=request.user.id)
		p.save()
		HoneyTip.objects.filter(slug=slug).update(scraps=F('scraps') + 1)
	else:
		fb = HoneyTipScrap.objects.get(slug=slug, user=request.user.id)
		fb.delete()
		HoneyTip.objects.filter(slug=slug).update(scraps=F('scraps') - 1)
	return redirect(request.META['HTTP_REFERER'])
