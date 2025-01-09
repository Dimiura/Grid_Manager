"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pilots.views import PilotListView,NewPilotCreateView, ObserveDetails, PilotUpdateView, DeleteView, NewTeamCreateView, TeamsListView, ObserveDetailsTeam, DeleteViewTeam, TeamUpdateView, AutodromosListView, ObserveDetailsAutodromos, content
from accounts.views import register_view, login_view, logout_view



urlpatterns = [
    path('admin/', admin.site.urls),
    # path ('pilots/', PilotListView.as_view(), name="pilots_list" ),
    # path ('teams/', TeamsListView.as_view(), name="teams_list" ),
    path ('home/', content , name="content" ),
    # path ('autodromos/', AutodromosListView.as_view(), name="autodromos_list" ),
    path ('register/', register_view, name="register"),
    path ('login/', login_view, name="login"),
    path ('logout/', logout_view, name="logout"),
    path ('new_pilot/', NewPilotCreateView.as_view(), name="new_pilot"),
    path ('new_team/', NewTeamCreateView.as_view(), name="new_team"),
    path ('pilots/<int:pk>/', ObserveDetails.as_view(), name="observe_pilot"),
    path ('teams/<int:pk>/', ObserveDetailsTeam.as_view(), name="observe_team"),
     path ('autodromo/<int:pk>/', ObserveDetailsAutodromos.as_view(), name="observe_autodromo"),
    path ('pilots/<int:pk>/update/', PilotUpdateView.as_view(), name="pilot_update"),
    path ('pilots/<int:pk>/delete/', DeleteView.as_view(), name="pilot_delete"),
    path ('teams/<int:pk>/update/', TeamUpdateView.as_view(), name="team_update"),
    path ('teams/<int:pk>/delete/', DeleteViewTeam.as_view(), name="team_delete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
