from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PropertySellForm

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