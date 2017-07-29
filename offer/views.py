# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def offer_list(request):
    return render(request, 'offer/offer_list.html', {})
