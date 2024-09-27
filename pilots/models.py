from django.db import models


class Team(models.Model):
      id = models.AutoField(primary_key=True)
      namet= models.CharField(max_length=200)

      def __str__(self):
            return self.namet

class Pilot(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    age = models.IntegerField( null=False, blank=False) 
    team = models.ForeignKey(Team, on_delete=models.PROTECT, related_name='pilots_team')
    avatar = models.ImageField (upload_to='pilots/', blank=True, null=True)
    
    def __str__(self):
            return self.name