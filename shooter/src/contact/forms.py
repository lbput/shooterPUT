from django import forms

from contact.simplemathcaptcha.fields import MathCaptchaField
from contact.simplemathcaptcha import utils


class ContactForm(forms.Form):
    name = forms.CharField(label=(u'Imię'), widget=forms.TextInput(attrs={'class':'form-control'}),max_length=50, required=True)
    email = forms.EmailField(label=(u'E-mail'), widget=forms.TextInput(attrs={'class':'form-control','type':'email'}),max_length=50, required=True)
    subject = forms.CharField(label=(u'Temat'), widget=forms.TextInput(attrs={'class':'form-control'}),max_length=100, required=True)
    message = forms.CharField(label=(u'Treść'),widget=forms.Textarea(attrs={'class':'form-control','rows':'3'}), required=True)

    captcha = MathCaptchaField(required=True)
