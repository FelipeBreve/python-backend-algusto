# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import gettext as _

# Create your views here.

def home(request):
    return render(request, 'home.html');

# def home(request):
#     data = {'name' : 'felipe', 'location': 'Brazil'}
#     return JsonResponse(data, status=200)
