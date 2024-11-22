from django.shortcuts import render, redirect, get_object_or_404
from pilots.models import Pilot, Team
from pilots.forms import FormCreation
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
            pilots = pilots.filter(model__icontains=search)
        return pilots

@method_decorator(login_required(login_url='login'), name='dispatch')   
class DeleteView(DeleteView):
    model = Pilot
    template_name = 'delete_pilot.html'
    success_url = '/pilots/'

@method_decorator(login_required(login_url='login'), name='dispatch')   
class NewPilotCreateView(CreateView):
    model = Pilot
    form_class = FormCreation
    template_name = 'new_pilot.html'
    success_url = '/pilots/'

class ObserveDetails(DetailView):
    model = Pilot
    template_name = 'detail_pilot.html'    

class PilotUpdateView(UpdateView):
    model = Pilot
    form_class = FormCreation
    template_name = "update_pilot.html"
    success_url = '/pilots/'

    def get_success_url(self):
        return reverse_lazy('detail_pilot', kwargs = {'pk': self.object.pk})