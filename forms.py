from django import forms


class Loginform(forms.Form):
    username= forms.CharField(max_length= 25,label="Enter username")
    password= forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)

class Signupform(forms.Form):
    firstname = forms.CharField(max_length=200, label='')
    lastname = forms.CharField(max_length=200, label='')
    email = forms.EmailField(label='')
