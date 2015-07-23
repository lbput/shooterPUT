from django import forms
from django.contrib.contenttypes.models import ContentType

from django.db import models
#from django.utils import timezone
#from pytz import timezone

from .models import CompetitionTournament, Tournament, Competition, CT_Payment

class TournamentOptionForm(forms.Form):
    pass
    #year = forms.ChoiceField(label='year', choices=())
    #tournament = forms.ChoiceField(label='tournament', choices=())
    #competition = forms.ChoiceField(label='competition', choices=())

    def __init__(self, *args, **kwargs):
        super(TournamentOptionForm, self).__init__(*args, **kwargs)
        #self.fields['year'].choices = [(0, '----')] + list(enumerate([date.split('-')[0] for date in map(str, CompetitionTournament.objects.all().dates('tournamentdate','year'))], start=1))

   
class TournamentSignUpForm(forms.Form):
    tour = forms.ChoiceField(label='Zawody', choices=(), required=True) 
    #tour = forms.ModelChoiceField(label='Zawody', queryset=(), required=True)
    comp = forms.ChoiceField(label='Konkurencje', choices=(), required=True)
    ammo = forms.BooleanField(label='Amunicja', initial=False, required=False)       
 
    def __init__(self, *args, **kwargs):
        super(TournamentSignUpForm, self).__init__(*args, **kwargs)
        from datetime import datetime
        self.fields['tour'].choices = [(0, '----')] + list(enumerate([tour_name for tour_name in map(str, CompetitionTournament.objects.filter(tournamentdate__gte=datetime.now()).values_list('tournament__tournamentname', flat=True).distinct())], start=1))     
        #self.fields['tour'].queryset = Tournamet.objects.all()


class TournamentResultsForm(forms.Form):
    year = forms.ChoiceField(label='year', choices=())
    tournament = forms.ChoiceField(label='tournament', choices=())
    competition = forms.ChoiceField(label='competition', choices=())
    
 
    def __init__(self, *args, **kwargs):
        super(TournamentResultsForm, self).__init__(*args, **kwargs)
        self.fields['year'].choices = [(0, '----')] + list(enumerate([date.split('-')[0] for date in map(str, CompetitionTournament.objects.all().datetimes('tournamentdate','year'))], start=1))
        #Article.objects.datetimes('date_publish', 'month', order='DESC')
