# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from .models import Offer

# Create your views here.
def offer_list(request):
    offers = Offer.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'offer/offer_list.html', {'offers':offers})

