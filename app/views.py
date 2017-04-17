"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
    request,
    'app/index.html',
        {
        'title':'Home Page',
        'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
    request,
    'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
    request,
    'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def honeytip(request):
    """Renders the honeytip page."""
    assert isinstance(request, HttpRequest)
    return render(
    request,
    'app/honeytip.html',
        {
            'title':'honeytip',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def delivery(request):
    """Renders the delivery page."""
    assert isinstance(request, HttpRequest)
    return render(
    request,
    'app/delivery.html',
        {
            'title':'delivery',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def recipe(request):
    """Renders the recipe page."""
    assert isinstance(request, HttpRequest)
    return render(
    request,
    'app/recipe.html',
        {
            'title':'recipe',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def randomcooking(request):
    """Renders the randomcooking page."""
    assert isinstance(request, HttpRequest)
    return render(
    request,
    'app/randomcooking.html',
        {
            'title':'randomcooking',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

