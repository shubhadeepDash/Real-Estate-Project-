from msilib.schema import Property
from django.shortcuts import render,redirect

import sys
sys.path.append('../property')
from property.models import Property
from property import urls

from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Maps
from django.contrib.auth.decorators import login_required
from geopy.geocoders import Nominatim
# Create your views here.


geolocator = Nominatim(user_agent="geoapiExercises")

# class AddressView(CreateView):

#     model = Maps
#     fields = ['address']
#     template_name = 'maps/sell.html'
#     success_url = 'maps/'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['mapbox_access_token'] = 'pk.eyJ1IjoidHVuYWhvYmJ5IiwiYSI6ImNra3IwaDNxcTBtbzAycm81dTFpOWhvcjAifQ.8ixXcuSDUuAlDSlazSLMCA'
#         context['addresses'] = Maps.objects.all()
#         return context

@login_required(login_url='login')
def sellProperty(request):
    if request.method == 'POST':
        lat = request.POST.get('latitude')
        long = request.POST.get('longitude')
        location = geolocator.reverse(lat+","+long)
        addr = location.raw['address']

        p = Property()
        
        p.seller = request.user
        p.title = request.POST.get('title')
        p.description = request.POST.get('description')
        p.length = request.POST.get('length')
        p.breadth = request.POST.get('breadth')
        p.price = request.POST.get('price')
        p.latitude = lat
        p.longitude = long
        p.city = addr.get('city','')
        p.state = addr.get('state','')
        p.country = addr.get('country','')
        p.pincode = addr.get('postcode')
        p.image = request.FILES.get('image')

        p.save()
        
    
    context={}
    return render(request,'maps/sell.html',context)




