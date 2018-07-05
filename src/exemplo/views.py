# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import gettext as _
from exemplo.models import Msg
from django.template import RequestContext

# Create your views here.

def home(req):
    if req.method == 'POST':
        p = req.POST
        req_author = p['author']
        req_msg = p['msg']

        if (req_author and req_msg):
            msg = Msg()
            max_content = Msg._meta.get_field('content').max_length
            max_author = Msg._meta.get_field('author').max_length

            msg.content = req_msg[0:max_content:]
            msg.author = req_author[0:max_content:]

            msg.save()

    context = {'msgs' : Msg.objects.all()}

    return render(req, 'home.html', context);

# def home(request):
#     data = {'name' : 'felipe', 'location': 'Brazil'}
#     return JsonResponse(data, status=200)
