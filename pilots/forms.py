from django.forms import ModelForm
from pilots.models import Pilot, Team, Autodromo


class FormCreation (ModelForm):
    class Meta:
        model = Pilot
        fields = ['name', 'pilot_age', 'team' , 'avatar', 'description', 'market_value', 'legend', 'situation', 'data_de_nascimento']

        labels = {
            'name':'Nome do Piloto',
            'pilot_age':'Idade',
            'team':'Equipe atual ou Última equipe',
            'description':'Sobre',
            'avatar': 'Imagem de Perfil',
            'market_value':'Valor de mercado',
            'legend':'Este piloto pode ser considerado como "Legend"?',
            'situation': 'Situação (Falecido, Aposentado ou Atividade)'
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)
        if user:
            self.fields['team'].queryset = Team.objects.filter(user=user)  

class FormCreationAutodromo (ModelForm):
    class Meta:
        model = Autodromo
        fields = ['name_autodromo', 'description_autodromo', 'ano_de_criacao_autodromo', 'recorde_tempo']

        labels = {
            'name_autodromo':'Nome do Autodromo',
            'description_autodromo': 'Sobre a pista', 
            'ano_de_criacao_autodromo': 'Ano de criação',
            'recorde_tempo':'Recorde registrado'
        }
    
class FormCreationTeam (ModelForm):
    class Meta:
        model = Team
        fields = ['namet', 'logo', 'legendteam', 'description_team', 'ano_de_criacao_team']

        labels = {
            'namet':'Nome da equipe',
            'logo': 'Logo da equipe', 
            'legendteam': 'Esta equipe pode ser considerada como "Legend"?',
            'ano_de_criacao_team':'Ano de Criação'
        }
