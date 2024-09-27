from django.shortcuts import render
from pilots.models import Pilot, Team



def pilots_view(request):
    pilots = Pilot.objects.all().order_by('name')
    search=request.GET.get('search')
    if search:
        pilots = Pilot.objects.filter(name__icontains = search)
    
    return render(request,
    'pilots.html',
    {'pilots': pilots })
