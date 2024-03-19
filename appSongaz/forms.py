from django import forms
from .models import File


class FileForm(forms.ModelForm):
    arrived = forms.CheckboxInput()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].widget.attrs.update({
            'class': 'form-control form-control-lg',  # Update input field classes
            'id': 'formFileLg',
            'type': 'file'
        })
        self.fields['arrived'].widget.attrs.update({
            'class': "form-check-input mx-3",
            'type': "checkbox",
            'id': "flexCheckDefault"
        })
        self.fields['arrived'].initial = True

    class Meta:
        model = File
        fields = ['file', 'arrived']
