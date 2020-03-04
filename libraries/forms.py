from django import forms
from . import models
from crispy_forms.helper import FormHelper


class LibraryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LibraryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = models.Library
        exclude = ['review', 'date_created']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'What is the name of the library?'}),
            'description': forms.Textarea(attrs={'rows': '5', 'placeholder': 'Tell us something about the library!'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput()
        }

        labels = {
            'picture': ''
        }

