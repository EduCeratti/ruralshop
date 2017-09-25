# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import OfferForm
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
    
    print("id eh: " + str(pk))
   
    Offer.objects.get(pk=pk)
    offer = get_object_or_404(Offer, pk=pk)
    return render(request, 'offer/offer_detail.html', {'offer': offer})

def offer_new(request):
    if request.method == "POST":
        form = OfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            #offer.customer_id = request.user
	    offer.customer_id = 1
            offer.created_date = timezone.now()
            offer.save()
            return redirect('offer_detail', pk=offer.pk)
    else:
        form = OfferForm()
    return render(request, 'offer/offer_edit.html', {'form': form})

def offer_edit(request, pk):
    offer = get_object_or_404(Offer, pk=pk)
    if request.method == "POST":
        form = OfferForm(request.POST, instance=offer)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.customer_id = 1
            offer.created_date = timezone.now()
            offer.save()
            return redirect('offer_detail', pk=offer.pk)
    else:
        form = OfferForm(instance=offer)
    return render(request, 'offer/offer_edit.html', {'form': form})

