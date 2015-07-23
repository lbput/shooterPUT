from django import forms
from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.db.models.loading import get_model
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from userprofile.models import User
from .models import Participant
from .dynamic_models import get_dynamic_model
from .dynamic_models import DynamicModelAttrs
from .forms import TournamentSignUpForm, TournamentResultsForm, TournamentOptionForm


@login_required
def tournament_option(request):
    ctx = {'form': TournamentOptionForm()}
    return render(request, "tournament_option.html", ctx)

@login_required
def tournament_signup(request): #logika w ajax.py
    ctx = {'form': TournamentSignUpForm()}
    return render(request, "tournament_signup.html", ctx)

@login_required
def tournament_results(request): #logika w ajax.py
    ctx = {'form': TournamentResultsForm()}
    return render(request, "tournament_results.html", ctx)