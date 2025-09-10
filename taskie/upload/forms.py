from django import forms
from .models import UploadModel

class DocumentForm(forms.ModelForm):
    class Meta:
        model = UploadModel
        fields = ['name', 'file']