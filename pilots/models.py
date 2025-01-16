from django.db import models
from django.contrib.auth.models import User 
from datetime import date


class Team(models.Model):
      id = models.AutoField(primary_key=True)
      namet= models.CharField(max_length=200)
      logo = models.ImageField (upload_to='logo_team/', blank=True, null=False)
      legendteam = models.BooleanField(null=True, default=False)
      description_team = models.TextField(null=True, blank=True)
      ano_de_criacao_team = models.IntegerField(null=True, blank=True)
      user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams', null=True, blank=True)

      def __str__(self):
            return self.namet
      
class Autodromo(models.Model):
      id = models.AutoField(primary_key=True)
      name_autodromo = models.CharField(max_length=150)
      ano_de_criacao_autodromo = models.IntegerField(null=True, blank=True)
      description_autodromo = models.TextField(null=True, blank=True)
      recorde_tempo = models.CharField(max_length=150)
      image = models.ImageField (upload_to='image/', blank=True, null=False)
      user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='autodromos', null=True, blank=True)

    
      def __str__(self):
            return self.name_autodromo
        

class Pilot(models.Model):
      id = models.AutoField(primary_key=True)
      name = models.CharField(max_length=150)
      pilot_age = models.IntegerField(null=True, blank=True)
      team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='pilots_team')  
      avatar = models.ImageField (upload_to='pilots/', blank=True, null=True)
      description = models.TextField(null=True, blank=True)
      market_value = models.FloatField(null=True, blank=True) 
      legend = models.BooleanField(null=True, default=False)
      situation = models.CharField(max_length=50, null=True, blank=True)
      data_de_nascimento = models.DateField(default="1800-01-01", blank=True)
      user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pilots', null=True, blank=True)
    
      def __str__(self):
            return self.name
      
class PilotInventory(models.Model):
      pilots_count = models.IntegerField()
      pilots_value = models.FloatField(null=True, blank=True)
      created_at = models.DateTimeField(auto_now_add=True)

      class Meta:
            ordering = ['-created_at']

      def __str__(self):
         return f'{self.pilots_count} - {self.pilots_value}'
            