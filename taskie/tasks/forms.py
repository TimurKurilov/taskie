from django import forms
from .models import Tasks

class TasksForm(forms.ModelForm):
    due_date = forms.DateField(
        input_formats=["%d.%m.%Y"],
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "placeholder": "дд.мм.гггг"
            }
        )
    )

    class Meta:
        model = Tasks
        fields = ["title", "description", "due_date"]
