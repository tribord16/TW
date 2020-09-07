"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title' : '......................................................................................................................................................',
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
            'title' : '......................................................................................................................................................',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title' : '......................................................................................................................................................',
            'year':datetime.now().year,
        }
    )
def items(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/items.html',
        {
            'title' : '......................................................................................................................................................',
            'year':datetime.now().year,
        }
    )

def payement(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/payement.html',
        {
            'title' : '......................................................................................................................................................',
            'year':datetime.now().year,
        }
    )
