from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError  


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser

        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number', 'password']
    
    
    def clean(self):
            cleaned_data = super().clean()

            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")
            

            if password and confirm_password:
                if password != confirm_password:
                    raise ValidationError( {"confirm_password": "Parollar mos kelmadi."})

    def clean_username(self):
            username = self.cleaned_data.get("username")


            if len(username) < 8:
                 raise ValidationError({"username": "Username 8 ta belgidan iborat bo'lsin"})   

            return username
    
    def clean_first_name(self):
         first_name = self.cleaned_data.get("first_name")
         return first_name
    
class LoginForm(forms.Form):
     username = forms.CharField(max_length= 10)
     password = forms.CharField(widget= forms.PasswordInput)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser

        fields = ['first_name', 'last_name', 'username', 'email', 'phone_number']
    
