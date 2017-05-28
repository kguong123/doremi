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
from .forms import *
from .models import HoneyTip, Contents


# Create your views here.


class HoneyTipLV(ListView) :
    model = HoneyTip
    template_name = 'honeytip/honeytip_all.html'
    context_object_name = 'honeytips'
    paginate_by = 8

class HoneyTipDV(DetailView) :
    model = HoneyTip


class HoneyTipCV(LoginRequiredMixin, CreateView):
    model = HoneyTip
    fields = ['title', 'slug','titleimage', 'viewcount','scraps', 'owner']
    initial = {'slug': 'auto-filling-do-not-input'}
    template_name = 'honeytip/honeytip_form.html'

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
            return redirect('honeytip/honeytip_all.html', pk=self.object.id)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class HoneyTipDeleteView(LoginRequiredMixin, DeleteView) :
    model = HoneyTip
    success_url = reverse_lazy('honeytip:index')
