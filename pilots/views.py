from django.shortcuts import render, redirect, get_object_or_404
from pilots.models import Pilot, Team
from pilots.forms import FormCreation
from django.views import View
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView




class PilotListView(ListView):
    model = Pilot
    template_name = 'pilots.html'
    context_object_name = 'pilots'

    def get_queryset(self):
        pilots = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')
        if search:
            pilots = pilots.filter(model__icontains=search)
        return pilots

    
def delete_pilot (request, pilot_id):
        
    pilot = get_object_or_404(Pilot, id=pilot_id)

    if request.method == "POST":
        pilot.delete()
        return redirect ('pilots_list')

    return render(request, 'delete_pilot.html', {'pilot': pilot})   
    

class NewPilotCreateView(CreateView):
    model = Pilot
    form_class = FormCreation
    template_name = 'new_pilot.html'
    success_url = '/pilots/'

class ObserveDetails(DetailView):
    model = Pilot
    template_name = 'detail_pilot.html'