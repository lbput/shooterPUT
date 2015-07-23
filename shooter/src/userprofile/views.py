from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings

from .forms import RegistrationForm, LoginForm, ChangePasswordForm, ChangeEmailForm, ResetPasswordForm
from .models import Person, User


def ShooterRegistration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/account/profile/')
	
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			person = Person(firstname = form.cleaned_data['firstname'],
							lastname = form.cleaned_data['lastname'],
							address = form.cleaned_data['address'],
							city = form.cleaned_data['city'],
							email = form.cleaned_data['email'],
							pesel = form.cleaned_data['pesel'])
			person.save()
			
			user = User.objects.create_user(person, form.cleaned_data['username'], password = form.cleaned_data['password'])
			user.save()

			return HttpResponseRedirect('/account/register-success/')
		else:
			if not ('password' in form.errors or 'password2' in form.errors or'firstname' in form.errors or'lastname' in form.errors or'username' in form.errors ):
				if 'Podany numer PESEL już istnieje w systemie.' in form.errors['pesel'] and 'Podany adres e-mail jest już powiązany z innym kontem w systemie.' in form.errors['email'] :
					try:
						person = Person.objects.get(pesel=form.data['pesel'],
													email = form.data['email'],
													firstname = form.cleaned_data['firstname'],
													lastname = form.cleaned_data['lastname'])
						user = User.objects.create_user(person, form.cleaned_data['username'], password = form.cleaned_data['password'])
						user.save()
						return HttpResponseRedirect('/account/register-success/')
					except Person.DoesNotExist:
						pass #ew. poinformować użytkownika że person o takim peselu i emailu już istnieje
			
			return render_to_response('register.html', {'form' : form }, context_instance=RequestContext(request))

	else:
		form = RegistrationForm()
		context = {'form' : form }
		return render_to_response('register.html', context, context_instance=RequestContext(request))

@login_required
def Profile(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/account/login/')
	shooter = request.user
	context = {'shooter' : shooter,
				'now' : timezone.localtime(timezone.now())} # dla testów

	return render_to_response('profile.html', context, context_instance=RequestContext(request))

def LoginRequest(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method=='POST':
		next = request.POST['next']
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(next)
				else:
					messages.error(request, 'Twoje konto jest nieaktywne.')
					return render_to_response('login.html', {'form' : form }, context_instance=RequestContext(request))
			else:
				messages.error(request, 'Błędny login i/lub hasło. Spróbuj jeszcze raz.')
				return render_to_response('login.html', {'form' : form, 'next' : next }, context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', {'form' : form, 'next' : next }, context_instance=RequestContext(request))
	else:
		next = request.GET.get('next','/')
		context = { 'next' : next }
		return render_to_response('login.html', context, context_instance=RequestContext(request))

@login_required
def LogoutRequest(request):
		logout(request)
		return HttpResponseRedirect('/')

def RegisterSuccess(request):
	return render_to_response("register-success.html", locals(), context_instance=RequestContext(request))

@login_required
def ChangePasswordRequest(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/account/login/')

	if request.method=='POST':
		form = ChangePasswordForm(user=request.user, data=request.POST or None)
		if form.is_valid():
			user = request.user
			user.set_password(form.cleaned_data['new_password'])
			user.save()
			return HttpResponseRedirect('/account/profile/')
		else:
			return render_to_response('change-password.html', {'form' : form }, context_instance=RequestContext(request))
	else:
		form = ChangePasswordForm()
		context = {'form' : form}
		return render_to_response('change-password.html', context, context_instance=RequestContext(request))

@login_required
def ChangeEmailRequest(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/account/login/')

	if request.method=='POST':
		form = ChangeEmailForm(user=request.user, data=request.POST or None)
		if form.is_valid():
			person = request.user.person
			person.email = form.cleaned_data['email']
			person.save()
			return HttpResponseRedirect('/account/profile/')
		else:
			return render_to_response('change-email.html', {'form' : form }, context_instance=RequestContext(request))
	else:
		form = ChangeEmailForm()
		context = {'form' : form}
		return render_to_response('change-email.html', context, context_instance=RequestContext(request))

def ResetPasswordRequest(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')

	if request.method=='POST':
		form = ResetPasswordForm(request.POST)
		if form.is_valid():
			person = Person.objects.get(email= form.cleaned_data['email'])
			user = User.objects.get(person=person)
			haslo = User.objects.make_random_password()
			user.set_password(haslo)
			user.save()
			message = """Twoje hasło do konta na portalu XXX zostało zresetowane.\n\nNazwa użytkownika: %s\nNowe hasło: %s""" % (
				user.username,
				haslo,)
			subject = 'Odzyskiwanie hasła'
			send_mail(subject, message, settings.EMAIL_HOST_USER, [form.cleaned_data['email']])
			return HttpResponseRedirect('/account/reset-success/')
		else:
			return render_to_response('reset-password.html', {'form' : form }, context_instance=RequestContext(request))
	else:
		form = ResetPasswordForm()
		context = {'form' : form}
		return render_to_response('reset-password.html', context, context_instance=RequestContext(request))

def ResetPasswordSuccessRequest(request):
	return render_to_response("reset-success.html", locals(), context_instance=RequestContext(request))
