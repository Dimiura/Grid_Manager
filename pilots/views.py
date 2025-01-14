from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from pilots.models import Pilot, Team, Autodromo
from pilots.forms import FormCreation, FormCreationTeam, FormCreationAutodromo
from django.views import View
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

class PilotListView(ListView):
    model = Pilot
    template_name = 'content.html'  
    context_object_name = 'pilots' 

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')  
        if search_query:
            return Pilot.objects.filter(name__icontains=search_query)  
        return Pilot.objects.all()  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_pilot'] = self.get_queryset().first()  
        return context

def pilot_search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        pilots = Pilot.objects.filter(name__icontains=search_query)
    else:
        pilots = Pilot.objects.all()

    data = [{'id': pilot.id, 'name': pilot.name, 'avatar': pilot.avatar.url, 
             'team': pilot.team.namet, 'team_logo': pilot.team.logo.url} for pilot in pilots]
    return JsonResponse({'pilots': data})    

def welcome (request):
    return render(request, 'partials/herobanner_welcome.html',)

@login_required
def content(request):
    teams = Team.objects.all()
    pilots = Pilot.objects.all().order_by('name')
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
    template_name = 'partials/delete_pilot.html'
    success_url = '/home/'

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
    success_url = '/home/'

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
    success_url = '/home/'

class ObserveDetails(DetailView):
    model = Pilot
    template_name = 'partials/modal_detail_pilot.html'    

class ObserveDetailsTeam(DetailView):
    model = Team
    template_name = 'partials/modal_detail_team.html'    

class ObserveDetailsAutodromos(DetailView):
    model = Autodromo
    template_name = 'partials/modal_detail_autodromo.html'        
        
    
@method_decorator(login_required(login_url='login'), name='dispatch') 
class PilotUpdateView(UpdateView):
    model = Pilot
    form_class = FormCreation
    template_name = "partials/update_pilot.html"
    success_url = '/home/'

    
@method_decorator(login_required(login_url='login'), name='dispatch') 
class TeamUpdateView(UpdateView):
    model = Team
    form_class = FormCreationTeam
    template_name = "partials/update_team.html"
    success_url = 'partials/teams/'

    def get_success_url(self):
        return reverse_lazy('observe_team', kwargs = {'pk': self.object.pk})   