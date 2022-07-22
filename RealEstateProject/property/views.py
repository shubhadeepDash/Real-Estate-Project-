from msilib.schema import Property
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PropertySellForm
from django.db.models import Q

def index(request):
    return render(request, 'property/home.html')

@login_required(login_url='login')
def sellProperty(request):
    form =  PropertySellForm()
    if request.method == 'POST':
        form =  PropertySellForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property-home')
    context = {"form": form}
    return render(request, "property/sell.html", context)

def results(request):
    q = request.GET.get('q')
    properties = Property.objects.filter(
        Q(city__icontains = q) |
        Q(state__icontains = q) |
        Q(country__icontains = q) |
        Q(pincode = int(q))
    )

    context = {'properties' : properties}

    return render(request,'property/results.html',context)