# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import gettext as _
from exemplo.models import Msg
from django.template import RequestContext

# Create your views here.

def home(req):
    if req.method == 'GET':
        return render(req, 'home.html');
    elif req.method == 'POST':
        p = req.POST
        author = p['author']
        msg = p['msg']

        if (author and msg):
            # TODO: Continuar essa bagaça...
            print("Fine!");

        return render(req, 'home.html');

# def home(request):
#     data = {'name' : 'felipe', 'location': 'Brazil'}
#     return JsonResponse(data, status=200)
