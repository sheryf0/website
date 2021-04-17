from django import forms 
from django.contrib.auth.forms import UserCreationForm
from accounts.models import student 
from django.contrib.auth import authenticate
from django.forms import ModelForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = student
        fields= ("first_name","last_name","email","phone","group_id","password1","password2")

        

class LoginForm(ModelForm ):
    password = forms.CharField(label = "password", widget= forms.PasswordInput)

    class Meta:
        model = student
        fields =("email", "password")

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password= self.cleaned_data['password']

            if  not authenticate(email = email , password= password):
                raise forms.ValidationError("your email or password is not correct check your spelings.....")



