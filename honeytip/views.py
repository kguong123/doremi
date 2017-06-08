# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.db import transaction
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from django.views.generic.edit import FormView
from django.db.models import Q

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from DjangoApp.views import LoginRequiredMixin
from django.shortcuts import redirect

from hitcount.views import HitCountDetailView

from .forms import *
from .models import HoneyTip, Contents

# Create your views here.


class HoneyTipLV(ListView) :
    model = HoneyTip
    template_name = 'honeytip/honeytip_all.html'
    queryset = HoneyTip.objects.order_by('-create_date')
    context_object_name = 'honeytips'
    paginate_by = 8

class HoneyTipScrapCountLV(ListView) :
    model = HoneyTip
    template_name = 'honeytip/honeytip_all.html'
    queryset = HoneyTip.objects.order_by('-scraps')
    context_object_name = 'honeytips'
    paginate_by = 8

#comment
class PostMixinDetailView(object):
    model = HoneyTip
    def get_context_data(self, **kwargs):
        context = super(PostMixinDetailView, self).get_context_data(**kwargs)
        context['post_list'] = HoneyTip.objects.all()[:5]
        return context

class HoneyTipDV(PostMixinDetailView, HitCountDetailView) :
    count_hit = True


class HoneyTipCV(LoginRequiredMixin, CreateView):
    model = HoneyTip
    fields = ['title', 'titleimage']

    def get_context_data(self, **kwargs):
        context = super(HoneyTipCV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = HoneyTipInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = HoneyTipInlineFormSet()
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
            return redirect('honeytip:index')
        else:
            return self.render_to_response(self.get_context_data(form=form))



class HoneyTipDeleteView(LoginRequiredMixin, DeleteView) :
    model = HoneyTip
    success_url = reverse_lazy('honeytip:index')

class BstrapSearchLV(ListView) :
    template_name = 'honeytip/post_bstrap_search.html'
    
    def get_queryset(self):
        schWord = '%s' % self.request.GET['search']
        post_list = HoneyTip.objects.filter(Q(title__icontains=schWord)).distinct() or HoneyTip.objects.filter(Q(contents__honeydescription__icontains=schWord)).distinct()
        self.search_term = schWord
        self.count = post_list.count()
        return post_list

    def get_context_data(self, **kwargs):
        context = super(BstrapSearchLV, self).get_context_data(**kwargs)
        context['search_term'] = self.search_term
        context['search_count'] = self.count
        return context