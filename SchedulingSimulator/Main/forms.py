from django import forms

class UserCreationForm(forms.Form):
    final_array = forms.CharField(widget=forms.HiddenInput())





