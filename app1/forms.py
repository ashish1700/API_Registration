from django.core import validators
from django import forms
from user.models import User


USER_TYPE_CHOICES = (
            ('superadmin', 'Super Admin'),
            ('admin', 'Admin'),
            ('student', 'Student'),
)
            
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widget = {
            'your_name' : forms.TextInput(attrs={'class':'form-control'}),
            'your_email' : forms.EmailInput(attrs={'class':'form-control'}),
            'your_password' : forms.PasswordInput(attrs={'class':'form-control'}),
            
                }
            # 'user_type' = forms.ChoiceField(choices = USER_TYPE_CHOICES)
            