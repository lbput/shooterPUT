import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType

from datetime import datetime
from .models import CompetitionTournament, Competition, Participant
from .dynamic_models import get_dynamic_model, DynamicModelAttrs


@csrf_exempt
def get_comp_for_tour(request):
    if request.is_ajax():
        if 'tour' in request.POST:
            data = {'0': '----'}
            try:
                for ct in CompetitionTournament.objects.filter(tournamentdate__gte=datetime.today(), 
                                                                tournament__tournamentname=request.POST['tour']):
                    data[ct.competition.id] = ct.competition.competitionname
            except ValueError:
                pass

            return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse()	




@csrf_exempt
def tournament_signup_ajax(request):
    if request.is_ajax():
        if 'tour' in request.POST and 'comp' in request.POST:
            ct = CompetitionTournament.objects.filter(tournamentdate__gte=datetime.today(),
                                                 tournament__tournamentname=request.POST['tour'],
                                                 competition__competitionname=request.POST['comp'])
            if ct:
                ct = ct[0]

            #checkbox
            if 'ammo' in request.POST:
                if request.POST['ammo'] == 'true':
            	    checkbox = 1
                else:
            	    checkbox = 0


            ct_id = ct.id
            result_tab = 'result_ct_%d' % ct_id
            pt_tab = 'paymenttournament_ct_%d' % ct_id
            rows = '10'

            
            person_id = request.user.person.id
            part = Participant.objects.get(id=person_id)

            dynAttr = DynamicModelAttrs()

 

            pt_model = get_dynamic_model(model_name=pt_tab, fields=dynAttr.get_pt_ct_attrs(pt_tab))
            pt_model.objects.create(participant=part,
                                    ct=ct,
                                    ammo=checkbox,
                                    payment_date=str(datetime.now()))

            
            result_model = get_dynamic_model(model_name=result_tab, fields=dynAttr.get_result_ct_attrs(result_tab))

            result_model.objects.create(participant=part,
                                        ct=ct,
                                        totalvalue=0)

            html = """ <p>OK</p> """

            return HttpResponse(json.dumps({'OK': html}), content_type="application/json")

    return HttpResponse()


@csrf_exempt
def get_tournaments(request):
    if request.is_ajax():
        if 'year' in request.POST:
            data = {'0': '----'}
            try:
                ct = CompetitionTournament.objects.filter(tournamentdate__year=request.POST['year'])
                for c in ct:
                    dynAttr = DynamicModelAttrs()
                    result_tab = 'result_ct_%d' % c.id
                    result_objects = get_dynamic_model(result_tab, dynAttr.get_result_ct_attrs(result_tab)).objects.all()

                    for obj in result_objects:
                        if obj.participant.person.id == request.user.person.id:
                            data[obj.ct.tournament.id] = obj.ct.tournament.tournamentname
                            continue
            except ValueError:
                pass

            return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse()


@csrf_exempt
def get_competitions(request):
    if request.is_ajax():
        if 'year' in request.POST and 'tour' in request.POST:
            data = {'0': '----'}
            try:
                ct = CompetitionTournament.objects.filter(tournamentdate__year=request.POST['year'],
                                                        tournament__tournamentname=request.POST['tour'])
                for c in ct:
                    dynAttr = DynamicModelAttrs()
                    result_tab = 'result_ct_%d' % c.id
                    result_objects= get_dynamic_model(result_tab, dynAttr.get_result_ct_attrs(result_tab)).objects.all()

                    for obj in result_objects:
                        if obj.participant.person.id == request.user.person.id:
                            data[obj.ct.competition.id] = obj.ct.competition.competitionname
                            continue
            except ValueError:
                pass

            return HttpResponse(json.dumps(data), content_type='application/json')

    return HttpResponse()


@csrf_exempt
def get_result_current_user(request):
    if request.is_ajax():
        if 'year' in request.POST and 'tour' in request.POST and 'comp' in request.POST:
            ct = CompetitionTournament.objects.filter(tournamentdate__year=request.POST['year'],
                                                 tournament__tournamentname=request.POST['tour'],
                                                 competition__competitionname=request.POST['comp'])

            if ct:
                ct = ct[0]

            table_id = ct.id
            rows = '10'


            html = """
                <table class="table table-striped">
                    <thead>
                        <th>Rank</th>
                    </thead>
                    <tbody>
                    <tr>
                    <td>%s</td>
                    </tr>
                    </tbody>
                </table>
            """ % (rows)

            return HttpResponse(json.dumps({'table': html}), content_type="application/json")

    return HttpResponse()