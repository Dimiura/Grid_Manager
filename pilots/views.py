from django.shortcuts import render, redirect, get_object_or_404
from pilots.models import Pilot, Team, Autodromo
from pilots.forms import FormCreation, FormCreationTeam, FormCreationAutodromo
from django.views import View
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class PilotListView(ListView):
    model = Pilot
    template_name = 'pilots.html'
    context_object_name = 'pilots'

    def get_queryset(self):
        pilots = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')
        if search:
            pilots = pilots.filter(name__icontains=search)
        return pilots

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['pilots']:
            context['first_pilot'] = context['pilots'][0]
        return context
    
def content(request):
    teams = Team.objects.all()
    pilots = Pilot.objects.all()
    autodromos = Autodromo.objects.all()
    context = {
        'pilots': pilots,
        'teams': teams,
        'autodromos':autodromos, 
    }
    return render(request, 'content.html', context)
    
class TeamsListView(ListView):
    model = Team
    template_name = 'content.html'
    context_object_name = 'teams'

    def get_queryset(self):
        teams = super().get_queryset().order_by('namet')
        search = self.request.GET.get('search')
        if search:
            teams = teams.filter(model__icontains=search)
        return teams
    
class AutodromosListView(ListView):
    model = Autodromo
    template_name = 'content.html'
    context_object_name = 'autodromos'

    def get_queryset(self):
        autodromos= super().get_queryset().order_by('name_autodromo')
        search = self.request.GET.get('search')
        if search:
            autodromos = autodromos.filter(model__icontains=search)
        return autodromos   

@method_decorator(login_required(login_url='login'), name='dispatch')   
class DeleteView(DeleteView):
    model = Pilot
    template_name = 'delete_pilot.html'
    success_url = '/pilots/'

@method_decorator(login_required(login_url='login'), name='dispatch')   
class DeleteViewTeam(DeleteView):
    model = Team
    template_name = 'delete_team.html'
    success_url = '/teams/'    

@method_decorator(login_required(login_url='login'), name='dispatch')   
class NewPilotCreateView(CreateView):
    model = Pilot
    form_class = FormCreation
    template_name = 'new_pilot.html'
    success_url = '/pilots/'

@method_decorator(login_required(login_url='login'), name='dispatch')   
class NewAutodromoCreateView(CreateView):
    model = Autodromo
    form_class = FormCreationAutodromo
    template_name = 'autodromo.html'
    success_url = '/autodromos/'    

@method_decorator(login_required(login_url='login'), name='dispatch')   
class NewTeamCreateView(CreateView):
    model = Team
    form_class = FormCreationTeam
    template_name = 'new_team.html'
    success_url = '/pilots/'

class ObserveDetails(DetailView):
    model = Pilot
    template_name = 'detail_pilot.html'    

class ObserveDetailsTeam(DetailView):
    model = Team
    template_name = 'detail_team.html'    

class ObserveDetailsAutodromos(DetailView):
    model = Autodromo
    template_name = 'detail_autodromo.html'        
        
    
@method_decorator(login_required(login_url='login'), name='dispatch') 
class PilotUpdateView(UpdateView):
    model = Pilot
    form_class = FormCreation
    template_name = "update_pilot.html"
    success_url = '/pilots/'

    def get_success_url(self):
        return reverse_lazy('observe_pilot', kwargs = {'pk': self.object.pk})
    
@method_decorator(login_required(login_url='login'), name='dispatch') 
class TeamUpdateView(UpdateView):
    model = Team
    form_class = FormCreationTeam
    template_name = "update_team.html"
    success_url = '/teams/'

    def get_success_url(self):
        return reverse_lazy('observe_team', kwargs = {'pk': self.object.pk})   