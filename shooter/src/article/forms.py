from django import forms
from .models import Article, Comment

from contact.simplemathcaptcha.fields import MathCaptchaField


class CommentForm(forms.ModelForm):
	first_name = forms.CharField(label=(u'Nick'), widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nick'}),max_length=50, required=True)
	body = forms.CharField(label=(u'Komentarz'),widget=forms.Textarea(attrs={'class':'form-control','rows':'3', 'placeholder':'Komentarz'}), max_length=1000, required=True)
	
	captcha = MathCaptchaField(required=True)

	class Meta:
		model = Comment
		fields = ('first_name', 'body')
