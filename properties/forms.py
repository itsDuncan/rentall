from django import forms
from .models import Property

class PropertyCreateForm(forms.ModelForm):
	class Meta:
		model = Property
		fields = ['name', 'address', 'image', 'rent', 'description', 'bedrooms', 'washrooms']

	name = forms.CharField(
		required = True,
		label = 'Property Name',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
			}),
	)

	address = forms.CharField(
		required = True,
		label = 'Address',
		widget = forms.TextInput(
			attrs = {
				'class': 'form-control',
			}),
	)

	image = forms.ImageField(
		required = False,
		widget = forms.FileInput(
			attrs = {
				'class': 'form-control',
			}),
	)

	rent = forms.IntegerField(
		required = True,
		label = 'Rent',
		widget = forms.NumberInput(
			attrs = {
				'class': 'form-control',
			}),
	)

	description = forms.CharField(
		required = True,
		label = 'Description',
		widget = forms.Textarea(
			attrs = {
				'class': 'form-control mb-3',
				'rows': 5,
		}),
	)

	bedrooms = forms.IntegerField(
		required = True,
		label = 'Bedrooms',
		widget = forms.NumberInput(
			attrs = {
				'class': 'form-control',
			}),
	)

	washrooms = forms.IntegerField(
		required = True,
		label = 'Washrooms',
		widget = forms.NumberInput(
			attrs = {
				'class': 'form-control',
			}),
	)