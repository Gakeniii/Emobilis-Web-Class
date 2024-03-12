
from django import forms
from .models import Registration,  Profile



class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=10)
    lastname = forms.CharField(max_length=10)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)       # enables us to put in the password
    class Meta:
        model = Registration
        fields = ['first_name', 'last_name', 'email', 'password']

class ProfileForm(forms.ModelForm):
    DOB = forms.DateField(widget=forms.DateInput)
    age = forms.IntegerField(widget=forms.NumberInput, min_value=18)
    class Meta:
        model = Profile
        fields = ['FirstName', 'LastName', 'age', 'DOB']