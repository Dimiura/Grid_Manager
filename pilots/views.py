from django.shortcuts import render, redirect, get_object_or_404
from pilots.models import Pilot, Team
from pilots.forms import FormCreation
from django.views import View
from django.urls import reverse




class Pilots(View):

    def get(self, request):
        pilots = Pilot.objects.all().order_by('name')
        search=request.GET.get('search')
        if search:
            pilots = Pilot.objects.filter(name__icontains = search)
        
        return render(request,
        'pilots.html',
        {'pilots': pilots })
    
    

def new_pilot_view(request):
    if request.method == "POST":
        new_pilot_form = FormCreation (request.POST, request.FILES)
        if new_pilot_form.is_valid:
            new_pilot_form.save()
            return redirect('pilots_list')
    else:
        new_pilot_form = FormCreation()
    return render (request, 'new_pilot.html', {'new_pilot_form': new_pilot_form})


def delete_pilot (request, pilot_id):
    
    pilot = get_object_or_404(Pilot, id=pilot_id)

    if request.method == "POST":
        pilot.delete()
        return redirect ('pilots_list')

    return render(request, 'delete_pilot.html', {'pilot': pilot})   
    