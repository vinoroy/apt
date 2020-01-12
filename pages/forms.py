from . models import Page, Apartment, Property, Size, Sector

from django.forms import ModelForm


class SizeForm(ModelForm):
    class Meta:
        model = Apartment
        fields = ['sizes']


class SectorForm(ModelForm):
    class Meta:
        model = Property
        fields = ['sector']

