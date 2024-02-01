
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm
from product.models import deatail

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password:',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password(again):',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={'username':forms.TextInput (attrs={'class':'form-control'}),'email':forms.TextInput (attrs={'class':'form-control'})}
        
class LoginForm(AuthenticationForm):
    username=forms.CharField(label="username",widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))   
    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))  
    
class Forgot(PasswordResetForm):
    username=forms.CharField(label="username",widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'})) 
    email=forms.EmailField(label="Email Adress",widget=forms.TextInput (attrs={'class':'form-control'}))
    password1=forms.CharField(label=' New Password:',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password(again):',widget=forms.PasswordInput(attrs={'class':'form-control'}))  

class DetailForm(forms.ModelForm):
    class Meta:
        model = deatail
        fields = ['name','address','payment_method','contact_number','email']
           
    

     
        