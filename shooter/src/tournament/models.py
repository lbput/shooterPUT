from django.db import models
from userprofile.models import Person

class ResultTemplate(models.Model):
    id = models.AutoField(db_column='ResultTemplateID', primary_key=True)
    point = models.BooleanField(db_column='Point')
    time = models.BooleanField(db_column='Time')
    func = models.CharField(db_column='Func', max_length=200)

    def __str__(self):
        return 'point = %s | time = %s | func = %s' % (self.point, self.time, self.func)

    class Meta:
        db_table = 'ResultTemplate'

class Competition(models.Model):
    id = models.AutoField(db_column='CompetitionID', primary_key=True)
    competitionname = models.CharField(db_column='CompetitionName', max_length=200)

    def __str__(self):
        return self.competition_name

    class Meta:
        db_table = 'Competition'

class Tournament(models.Model):
    id = models.AutoField(db_column='TournamentID', primary_key=True)
    tournamentname = models.CharField(db_column='TournamentName', max_length=200)

    def __str__(self):
        return self.tournament_name

    class Meta:
        db_table = 'Tournament'

class CompetitionTournament(models.Model):
    id = models.AutoField(db_column='CompetitionTournamentID', primary_key=True) 
    tournament = models.ForeignKey('Tournament', db_column='TournamentID')
    competition = models.ForeignKey('Competition', db_column='CompetitionID')
    trial = models.IntegerField(db_column='Trial')
    rated = models.IntegerField(db_column='Rated')
    tournamentdate = models.DateTimeField(db_column='TournamentDate')
    columnsresult = models.IntegerField(db_column='ColumnsResult')
    rt = models.ForeignKey(ResultTemplate, db_column='RT_ID')
    
    class Meta:
        db_table = 'CompetitionTournament'

    def __str__(self):
        return '%s - %s (%s)' % (self.tournament.tournament_name, self.competition.competition_name, self.tournament_date)

class CT_Payment(models.Model):
    id = models.AutoField(db_column='CT_PaymentID', primary_key=True)
    ct = models.OneToOneField('CompetitionTournament', db_column='CT_ID')   #OneToOneField is merely just ForeignKey(unique=True)
    start_payment = models.DecimalField(db_column='StartPayment', max_digits=5, decimal_places=2)
    ammo_payment = models.DecimalField(db_column='AmmoPayment', max_digits=5, decimal_places=2)

    def __str__(self):
        return '%s | starting fee: %s | ammo fee: %s' % (self.ct, self.start_payment, self.ammo_payment)

    class Meta:
        db_table = 'CT_Payment'

#---
#Participant++ Models
#---

#class ClubMember(models.Model):
#    id = models.AutoField(db_column='ClubMemberID', primary_key=True)
#    person = models.ForeignKey(Person, db_column='PersonID', unique=True)
#    joineddate = models.DateTimeField(db_column='JoinedDate', default=timezone.now)
#    leftdate = models.DateTimeField(db_column='LeftDate', null=True, blank=True)

#    def __unicode__(self):
#        return '%s %s' % (self.person.firstname, self.person.lastname)

#    class Meta:
#        db_table = 'ClubMember'

#class PaymentClub(models.Model):
#    id = models.IntegerField(db_column='PaymentClubID', primary_key=True) 
#    clubmember = models.ForeignKey(ClubMember, db_column='ClubMemberID')
#    paymentname = models.CharField(db_column='PaymentName', max_length=255, null=True, blank=True)
#    paymentdate = models.DateTimeField(db_column='PaymentDate', null=True, blank=True)

#    def __unicode__(self):
#        return '%s %s' % (self.clubmember.person.firstname, self.clubmember.person.lastname)

#    class Meta:
#        db_table = 'PaymentClub'

class Club(models.Model):
    id = models.AutoField(db_column='ClubID', primary_key=True)
    clubname = models.CharField(db_column='ClubName', max_length=200, unique=True)
    isactive = models.BooleanField(db_column='IsActive', default=True)

    def __str__(self):
        return '%s' % self.clubname

    class Meta:
        db_table = 'Club'


class Participant(models.Model):
    id = models.AutoField(db_column='ParticipantID', primary_key=True)
    person = models.ForeignKey(Person, db_column='PersonID', unique=True)
    club = models.ForeignKey(Club,  db_column='ClubID', blank=True, null=True)

    def __str__(self):
        return '%s %s - %s' % (self.person.firstname, self.person.lastname, self.club.clubname)

    class Meta:
        db_table = 'Participant'

