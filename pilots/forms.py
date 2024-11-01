from django.forms import ModelForm
from pilots.models import Pilot

class FormCreation (ModelForm):
    class Meta:
        model = Pilot
        fields = ['name', 'age', 'team']