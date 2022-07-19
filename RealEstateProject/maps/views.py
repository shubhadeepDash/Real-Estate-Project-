from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Maps


class AddressView(CreateView):

    model = Maps
    fields = ['address']
    template_name = 'maps/sell.html'
    success_url = 'maps/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoidHVuYWhvYmJ5IiwiYSI6ImNra3IwaDNxcTBtbzAycm81dTFpOWhvcjAifQ.8ixXcuSDUuAlDSlazSLMCA'
        context['addresses'] = Maps.objects.all()
        return context