from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=100, label='todo_list', widget=forms.TextInput(attrs={'placeholder': ' '}))