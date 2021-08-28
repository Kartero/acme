from django import forms
from django.forms.widgets import DateInput
from .models import Action, Sport
import datetime

class ActionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ActionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Action
        fields = ['date', 'sport', 'value']
        widgets = {
            'date': DateInput(attrs={'value': datetime.date.today, 'type': 'date'})
        }
