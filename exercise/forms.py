from django import forms
from .models import Sport
import datetime

class ActionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(ActionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    date = forms.DateField(label='Päiväys', initial=datetime.date.today)
    sport = forms.ModelChoiceField(label='Laji', queryset=Sport.objects.all())
    value = forms.DecimalField(label='Matka')