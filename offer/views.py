# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Offer

# Create your views here.
def offer_list(request):

    search = request.GET.get('search_box')
    if request.method == 'GET' and search:
        # Icontains por conta de ser insentitive
        offers=Offer.objects.filter(title__icontains = request.GET.get('search_box', None)) 
    else:
        offers = Offer.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    
    return render(request, 'offer/offer_list.html', {'offers':offers})

def offer_detail(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    return render(request, 'offer/offer_detail.html', {'offer': offer})


