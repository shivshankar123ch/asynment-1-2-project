
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import Post


class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'fist_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
  'first_name':forms.TextInput(attrs={'class':'form-control'}),
  'last_name':forms.TextInput(attrs={'class':'form-control'}),
  'email':forms.EmailInput(attrs={'class':'form-control'}),
  }
        
class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("password"),strip=False,
    widget=forms.PasswordInput(attrs={'autocomplet':'current-password','class':'form-control'}))  

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ["title","desc"]
        labels={'title':'Title','desc':'Descripsion'}
        Widget={'title':forms.TextInput(attrs={'class':'forms-control'}),
        'desc':forms.Textarea(attrs={'class':'forms-control'}),}
        
     
        
