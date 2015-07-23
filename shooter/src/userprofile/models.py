from django.db import models
from django.utils.encoding import smart_text
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Person(models.Model):
	id = models.AutoField(db_column='PersonID', primary_key=True)
	firstname = models.CharField(db_column='FirstName', max_length=200)
	lastname = models.CharField(db_column='LastName', max_length=200)
	address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)
	city = models.CharField(db_column='City', max_length=200, blank=True, null=True)
	email = models.EmailField(db_column='Email', unique=True)
	pesel = models.CharField(db_column='PESEL', unique=True, max_length=11)

	class Meta:
		db_table = 'Person'

	def __str__(self):
		return self.email

class CustomUserManager(BaseUserManager):
	def create_user(self, person, username, password=None, ):
		if not username:
			raise ValueError('username jest wymagane')

		cuser = self.model(person=person, username=username, is_active=True,)
		cuser.set_password(password)
		cuser.save(using=self._db)
		return cuser

	def create_superuser(self, username, password=None, ):
		try:
			c=Person.objects.latest('id').id
		except Person.DoesNotExist:
			  c=0
		pes=str(c+1).zfill(11)
		p = Person(id=c+1, firstname='Administartor', lastname='Administratorski',email=username+'@admin.com',pesel=pes)
		p.save()
		u = self.create_user(p, username, password, )
		u.is_admin = True
		u.save(using=self._db)
		return u

class User(AbstractBaseUser):
	id = models.AutoField(db_column='UserID', primary_key=True) # 
	username = models.CharField(db_column='UserName', max_length=200, unique=True) # 
	person = models.ForeignKey(Person, db_column='PersonID', unique=True) # 
	is_active = models.BooleanField(db_column='IsActive', default=True) # 
	is_admin = models.BooleanField(db_column='IsAdmin', default=False) # 

	objects = CustomUserManager()

	USERNAME_FIELD = 'username'

	class Meta:
		db_table = 'User'

	def get_full_name(self):
		return self.username

	def get_short_name(self):
		return self.username

	@property
	def is_superuser(self):
		return self.is_admin

	@property
	def is_staff(self):
		return self.is_admin

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return self.is_admin

class Clubmember(models.Model):
	clubmemberid = models.AutoField(db_column='ClubMemberID', primary_key=True)
	person = models.ForeignKey(Person, db_column='PersonID', unique=True)
	joineddate = models.DateTimeField(db_column='JoinedDate')
	leftdate = models.DateTimeField(db_column='LeftDate', blank=True, null=True)
	
	class Meta:
		db_table = 'ClubMember'
	
	def __str__(self):
		return self.person.email
