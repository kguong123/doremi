# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from django.views.generic.edit import FormView
from django.db.models import Q

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from DjangoApp.views import LoginRequiredMixin


# Create your views here.
class delivery(LoginRequiredMixin, TemplateView) :
    template_name = 'templates/delivery.html'

def selectcompany(request):
	if request.GET.get('company') == '1':
		url= 'http://nplus.doortodoor.co.kr/web/detail.jsp?slipno=%s' % request.GET['number']
		return redirect(url)		
	elif request.GET.get('company') == '2':
		url = 'http://d2d.ilogen.com/d2d/delivery/invoice_tracesearch_quick.jsp?slipno=%s'  % request.GET['number']
		return redirect(url)	
	elif request.GET.get('company') == '3':
		url = 'http://www.hlc.co.kr/hydex/jsp/tracking/trackingViewCus.jsp?InvNo=%s'  % request.GET['number']
		return redirect(url)
	elif request.GET.get('company') == '4':
		url = 'http://www.hanjin.co.kr/Delivery_html/inquiry/result_waybill.jsp?wbl_num=%s'  % request.GET['number']
		return redirect(url)
	elif request.GET.get('company') == '5':
		url = 'http://service.epost.go.kr/trace.RetrieveRegiPrclDeliv.postal?sid1=%s'  % request.GET['number']
		return redirect(url)
	elif request.GET.get('company') == '6':
		url = 'http://www.doortodoor.co.kr/jsp/cmn/TrackingCVS.jsp?pTdNo=%s'  % request.GET['number']
		return redirect(url)
	elif request.GET.get('company') == '7':
		url = 'http://www.kgbls.co.kr//sub5/trace.asp?f_slipno=%s'  % request.GET['number']
		return redirect(url)
	elif request.GET.get('company') == '8':
		url = 'http://www.kglogis.co.kr/delivery/popup_tracking.jsp?item_no=%s'  % request.GET['number']
		return redirect(url)