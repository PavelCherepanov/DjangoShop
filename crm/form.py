from django import forms

class SubscribeForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=200, widget=forms.TextInput(attrs={'class':'nl-email'}))
    email = forms.EmailField(label='Email', max_length=200, widget=forms.EmailInput(attrs={'class':'nl-email'}))