from django.db import models
from django.db import connection
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from .models import Participant
from .models import CompetitionTournament


class DynamicModelAttrs(object):
    def __init__(self, *args, **kwargs):
        super(DynamicModelAttrs, self).__init__()


    def get_result_ct_attrs(self, model_name):
        attr = {
            'id': models.AutoField(db_column='ResultID', primary_key=True),
            'participant': models.ForeignKey(Participant, db_column='ParticipantID'),
            'ct': models.ForeignKey(CompetitionTournament, db_column='CT_ID'),
            'totalvalue': models.DecimalField(db_column='TotalValue', max_digits=7, decimal_places=3),
            'number_10': models.DecimalField(db_column='Number_10', null=True, blank=True),
            'number_9': models.DecimalField(db_column='Number_9',null=True, blank=True),
            'number_8': models.DecimalField(db_column='Number_8',null=True, blank=True),
            'number_7': models.DecimalField(db_column='Number_7',null=True, blank=True),
            'number_6': models.DecimalField(db_column='Number_6',null=True, blank=True),
            'number_5': models.DecimalField(db_column='Number_5',null=True, blank=True),
            'number_4': models.DecimalField(db_column='Number_4',null=True, blank=True),
            'number_3': models.DecimalField(db_column='Number_3',null=True, blank=True),
            'number_2': models.DecimalField(db_column='Number_2',null=True, blank=True),
            'number_1': models.DecimalField(db_column='Number_1',null=True, blank=True),
            'number_0': models.DecimalField(db_column='Number_0',null=True, blank=True),
            '__module__': 'tournament.models',
            'Meta': type('Meta', (object, ), {
                'db_table': '%s' % (model_name)
            })
        }
        return attr

    def get_pt_ct_attrs(self, model_name):
        attr = {
            'id': models.AutoField(db_column='PaymentTournamentID', primary_key=True),
            'participant': models.ForeignKey(Participant, db_column='ParticipantID'),
            'ct': models.ForeignKey(CompetitionTournament, db_column='CT_ID'),
            'ammo': models.BooleanField(db_column='Ammo', default=False),
            'payment_date': models.DateTimeField(db_column='PaymentDate'),
            '__module__': 'tournament.models',
            'Meta': type('Meta', (object, ), {
                'db_table': '%s' % (model_name)
            })
        }
        return attr


    def get_shot_ct_attrs(self, model_name):
        attr = {
            'id': models.AutoField(db_column='ShotID', primary_key=True),
            #'result' = models.ForeignKey(!!result_ct_!!, db_column='ResultID')

            #'result': models.ForeignKey(ContentType),
            #'object_id': models.IntegerField(),

            'participant': models.ForeignKey(Participant, db_column='ParticipantID'),
            'numberofshot': models.IntegerField(db_column='NumberOfShot'),
            'value': models.DecimalField(db_column='Value', max_digits=5, decimal_places=3),
            '__module__': 'tournament.models',
            'Meta': type('Meta', (object, ), {
                'db_table': '%s' % (model_name)
            })
        }
        return attr


def get_dynamic_model(model_name, fields):
    return type(model_name, (models.Model,), fields)
