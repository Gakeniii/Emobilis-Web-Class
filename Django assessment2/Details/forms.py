from django import forms
from Details.models import Registration, Employee_details

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'phone_number', 'password']

class Employee_details_form(forms.ModelForm):
    class Meta:
        model = Employee_details
        fields = ['fullname', 'ID_no', 'phone_number']