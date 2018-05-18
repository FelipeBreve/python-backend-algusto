# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def home(request):
    context = {'bem_vindo' : 'Bem vindo ao projeto de python Manitos'}
    return render(request, 'home.html', context);

# def home(request):
#     data = {'name' : 'felipe', 'location': 'Brazil'}
#     return JsonResponse(data, status=200)