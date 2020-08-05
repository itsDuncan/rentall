from django import forms
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ChangePasswordForm
from .models import User

class RentManLoginForm(LoginForm):

	def __init__(self, *args, **kwargs):
		super(RentManLoginForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
			})

class RentManSignupForm(SignupForm):

	def __init__(self, *args, **kwargs):
		super(RentManSignupForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
			})

class RentManResetPasswordForm(ResetPasswordForm):

	def __init__(self, *args, **kwargs):
		super(RentManResetPasswordForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
				'placeholder': '',
			})

class RentManChangePasswordForm(ChangePasswordForm):

	def __init__(self, *args, **kwargs):
		super(RentManChangePasswordForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
				'placeholder': '',
			})

class RegisterTenantForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'firstname', 'lastname', 'phone_number', 'email', 'occupation', 'kra']

	def __init__(self, *args, **kwargs):
		super(RegisterTenantForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
				'placeholder': '',
			})