from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    # first_name = forms.CharField(label='Username',
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(
    #     attrs={'class': 'form-control',
    #            'placeholder': 'First Name',
    #            'type': 'text',
    #            'id': 'first_name'
    #            }
    #     ))

    # last_name = forms.CharField(label='Имя',
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(
    #     attrs={'class': 'form-control',
    #            'placeholder': 'Last Name',
    #            'type': 'text',
    #            'id': 'last_name'
    #            }
    #     ))

    # email = forms.CharField(label='Email',
    #     max_length=100,
    #     required=True,
    #     widget=forms.TextInput(
    #     attrs={'class': 'form-control',
    #            'placeholder': 'Email',
    #            'type': 'text',
    #            'id': 'email'
    #            }
    #     ))

    countries = [('usa', 'United States'), ('uk', 'United Kingdom'), ('ger', 'Germany'), ('fra', 'France')]
    country = forms.ChoiceField(widget=forms.Select, choices=countries)

    street_address = forms.CharField(label='Address',
        max_length=100,
        required=True,
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Address',
            'type': 'text',
            'id': 'street_address',
        }))

    city = forms.CharField(label='City',
        help_text=False,
        max_length=100,
        required=True,
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'City',
            'type': 'text',
            'id': 'city',
        }))

    zip_code = forms.CharField(label='ZipCode',
        help_text=False,
        max_length=100,
        required=True,
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Zip Code',
            'type': 'text',
            'id': 'zipCode',
        }))

    comment = forms.CharField(label='Comment',
        help_text=False,
        max_length=100,
        required=False,
        widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment',
            'type': 'text',
            'id': 'comment',
        }))
    class Meta:
        model = Order
        fields = ('country', 'street_address', 'city', 'zip_code', 'comment')