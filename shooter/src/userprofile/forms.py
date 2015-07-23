from django import forms
from .models import Person, User


class RegistrationForm(forms.ModelForm):
	firstname = forms.CharField(label=(u'Imię'),widget=forms.TextInput(attrs={'class':'form-control'}))
	lastname = forms.CharField(label=(u'Nazwisko'),widget=forms.TextInput(attrs={'class':'form-control'}))
	address = forms.CharField(label=(u'Adres'),widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
	city = forms.CharField(label=(u'Miasto'),widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
	pesel = forms.CharField(label=(u'PESEL'),widget=forms.TextInput(attrs={'class':'form-control', 'maxlength':'11'}))
	email = forms.EmailField(label=(u'E-mail'),widget=forms.TextInput(attrs={'class':'form-control','type':'email'}))
	username = forms.CharField(label=(u'Login'),widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(label=(u'Hasło'), widget=forms.PasswordInput(attrs={'class':'form-control'},render_value=False))
	password2 = forms.CharField(label=(u'Powtórz hasło'), widget=forms.PasswordInput(attrs={'class':'form-control'}, render_value=False))
	
	class Meta:
		model = Person

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("Użytkownik o podanym loginie już istnieje w systemie.")

	def clean_email(self):
		email = self.cleaned_data['email']
		try:			
			Person.objects.get(email=email)
		except Person.DoesNotExist:
			return email
		raise forms.ValidationError("Podany adres e-mail jest już powiązany z innym kontem w systemie.")

	def clean_pesel(self):
		pesel = self.cleaned_data['pesel']
		if not pesel.isdigit():
			raise forms.ValidationError("Pole zawiera niewłaściwe znaki.") 
		if len(pesel) != 11:
			raise forms.ValidationError("Podany numer PESEL ma nieodpowiednią długość.")
		try:			
			Person.objects.get(pesel=pesel)
		except Person.DoesNotExist:
			return pesel
		raise forms.ValidationError("Podany numer PESEL już istnieje w systemie.")

	def clean_password(self):
		data = self.data
		if "password" in data and "password2" in data and data["password"] != data["password2"]:
			raise forms.ValidationError("Podane hasła różnią się.")

	def clean_password2(self):
		data2 = self.data
		if "password" in data2 and "password2" in data2 and data2["password"] != data2["password2"]:
			raise forms.ValidationError("Podane hasła różnią się.")


class LoginForm(forms.Form):
		username = forms.CharField(label=(u'Login'))
		password = forms.CharField(label=(u'Hasło'), widget=forms.PasswordInput(render_value=False))


class ChangePasswordForm(forms.Form):
	old_password = forms.CharField(label=(u'Aktualne hasło'), widget=forms.PasswordInput(attrs={'class':'form-control'},render_value=False))
	new_password = forms.CharField(label=(u'Nowe Hasło'), widget=forms.PasswordInput(attrs={'class':'form-control'},render_value=False))
	new_password2 = forms.CharField(label=(u'Powtórz nowe hasło'), widget=forms.PasswordInput(attrs={'class':'form-control'},render_value=False))

	def __init__(self, user=None, data=None):
		self.user = user
		super(ChangePasswordForm, self).__init__(data=data)

	def clean_old_password(self):
		password = self.cleaned_data.get('old_password', None)
		if not self.user.check_password(password):
			raise forms.ValidationError("Podane hasło jest błędne.")
	
	def clean_new_password(self):
		data = self.data
		if "new_password" in data and "new_password2" in data and data["new_password"] != data["new_password2"]:
			raise forms.ValidationError("Podane hasła różnią się.")

	def clean_new_password2(self):
		data2 = self.data
		if "new_password" in data2 and "new_password2" in data2 and data2["new_password"] != data2["new_password2"]:
			raise forms.ValidationError("Podane hasła różnią się.")


class ChangeEmailForm(forms.Form):
	email = forms.EmailField(label=(u'Nowy adres e-mail'),widget=forms.TextInput(attrs={'class':'form-control','type':'email'}))
	current_password = forms.CharField(label=(u'Aktualne hasło'), widget=forms.PasswordInput(attrs={'class':'form-control'},render_value=False))

	def __init__(self, user=None, data=None):
		self.user = user
		super(ChangeEmailForm, self).__init__(data=data)

	def clean_current_password(self):
		password = self.cleaned_data.get('current_password', None)
		if not self.user.check_password(password):
			raise forms.ValidationError('Podane hasło jest błędne.')


class ResetPasswordForm(forms.Form):
	email = forms.EmailField(label=(u'Adres e-mail przypisany do konta'),widget=forms.TextInput(attrs={'class':'form-control','type':'email'}))

	def clean_email(self):
		try:
			Person.objects.get(email= self.cleaned_data['email'])
			return self.cleaned_data['email']
		except Person.DoesNotExist:
			raise forms.ValidationError('Błędny adres e-mail.')
