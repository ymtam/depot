from django.forms import ModelForm, fields, models
from trains.models import train

class LocationForm(ModelForm):
    class Meta:
        model = train
        fields = ['tid','location','status']