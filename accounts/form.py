from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSignUpFormTelegram(forms.Form):
    telegram_name = forms.CharField(label='Telegram',
        max_length=100,
        required=True,
        widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'telegram',
               'type': 'text',
               'id': 'telegram_name'
               }
        ))

class UserSignUpForm(UserCreationForm):
    """User registration form."""

    username = forms.CharField(label='Username',
        max_length=100,
        required=True,
        widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'username',
               'type': 'text',
               'id': 'user_name'
               }
        ))

    

    first_name = forms.CharField(label='Имя',
        max_length=100,
        required=True,
        widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Имя',
               'type': 'text',
               'id': 'first_name'
               }
        ))

    last_name = forms.CharField(label='Фамилия',
        max_length=100,
        required=True,
        widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Фамилия',
               'type': 'text',
               'id': 'last_name'
               }
        ))

    email = forms.EmailField(label='Email',
        max_length=254,
        required=True,
        widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'email',
               'type': 'text',
               'id': 'email_address'
               }
        ))

    password1 = forms.CharField(label='Пароль',
        help_text="<ul class='errorlist text-muted'><li>Ваш пароль должен содержать не менее 8 символов.</li></ul>",
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Пароль',
            'type': 'password',
            'id': 'user_password',
        }))

    password2 = forms.CharField(label='Confirm password',
        help_text=False,
        max_length=100,
        required=True,
        widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль',
            'type': 'password',
            'id': 'user_password',
        }))

    class Meta:
        model = User
        fields = ( 'username', 'first_name', 'last_name', 'email', 'password1', 'password2', )