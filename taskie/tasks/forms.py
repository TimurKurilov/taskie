from django import forms
from .models import Tasks

class TasksForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        input_formats=['%d.%m.%Y', '%Y-%m-%d'],
        help_text="Введите дату в формате ДД.ММ.ГГГГ или выберите в календаре"
    )

    class Meta:
        model = Tasks
        fields = ["title", "description", "due_date"]
