from django.template import RequestContext
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail

from .forms import ContactForm


def contact_form(request):
	if request.POST:
		form = ContactForm(request.POST)
		if form.is_valid():
			# Imaginable form purpose. Post to admins.
			message = """From: %s <%s>\r\nSubject: %s\r\nMessage:\r\n%s\r\n""" % (
				form.cleaned_data['name'],
				form.cleaned_data['email'],
				form.cleaned_data['subject'],
				form.cleaned_data['message']
			)
			subject = form.cleaned_data['subject']
			receiver = form.cleaned_data['email']
			send_mail(subject, message, receiver, settings.LIST_OF_EMAIL_RECIPIENTS)

			return HttpResponseRedirect('/contact/thank-you/')

		else:
			return render(request, 'contact.html', {'form':form},context_instance=RequestContext(request))
	else:
		form = ContactForm()
		return render(request, 'contact.html', {'form':form},context_instance=RequestContext(request))

def thank_you(request):
	return render(request, 'thankyou.html')
