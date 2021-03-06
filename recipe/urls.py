"""hihi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', RecipeLV.as_view(), name='index'),
    url(r'^recent/$', RecipeScrapCountLV.as_view(), name='scrap_order'),
    url (r'^bssearch/$', BstrapSearchLV.as_view(), name='bssearch'),
    url(r'^add/$', RecipeCV.as_view(), name='add'),
    url(r'^(?P<slug>[-\w]+)/$', RecipeDV.as_view(), name='recipe_detail'),
    url(r'^(?P<slug>[-\w]+)/delete/$',RecipeDeleteView.as_view(), name="delete"),
    url(r'^(?P<pk>[0-9]+)/update/$',RecipeUV.as_view(), name="recipe_update"),
    url(r'^(?P<slug>[-\w]+)/savecomment/$', SaveComments, name='savecomment'),
    url(r'^(?P<pk>[0-9]+)/deletecomment/$', deletecomment, name='deletecomment'),
]
