from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.db.models import F
from django.views.generic.edit import CreateView
from .forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from mypage.models import HomeVisitorsRecord
from django.contrib.auth.models import User
from recipe.models import Recipe
from honeytip.models import HoneyTip
import datetime
# Create your views here.

#--- TemplateView
def HomeView(request) :
	today=datetime.datetime.today()
	ck = HomeVisitorsRecord.objects.filter(date=today.strftime("%Y-%m-%d")).count()
	if ck == 0:
		p = HomeVisitorsRecord(todaycount=1, date=today.strftime("%Y-%m-%d"))
		p.save()
	else :
		HomeVisitorsRecord.objects.filter(date=today.strftime("%Y-%m-%d")).update(todaycount=F('todaycount') + 1)
	todayvisitors = HomeVisitorsRecord.objects.filter(date=today.strftime("%Y-%m-%d"))
	Honeytotal = HoneyTip.objects.all().count()
	recipetotal = Recipe.objects.all().count()
	total=Honeytotal+recipetotal
	usercount = User.objects.all().count()
	return render(request, 'home.html', {'todayvisitors': todayvisitors, 'total': total, 'usercount':usercount})

#--- User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')
    
    

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

#--- @login_required
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)
