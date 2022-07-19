import geocoder

from django.db import models


mapbox_access_token = 'pk.eyJ1IjoiaXNvdXJhdjciLCJhIjoiY2w1cnp1YW9sMWZpNjNjcGM0M3k4b2I0aiJ9.l3m47fOfsKpPjmww0HKfJw'

class Maps(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Maps, self).save(*args, **kwargs)