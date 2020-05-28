from django import forms

class UserCreationForm(forms.Form):
    final_array = forms.CharField(widget=forms.HiddenInput())
    interval = forms.CharField(label='Interval', max_length=5, initial=0)
    noOfTasks = forms.CharField(widget=forms.HiddenInput())





