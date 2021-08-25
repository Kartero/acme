from django.db import models
from django.db.models.enums import IntegerChoices
from django.utils.translation import gettext as _

class Sport(models.Model):

    class Types(models.IntegerChoices):
        KM = 1,_('Km')
        COUNT = 2,_('Count')

    name = models.CharField(max_length=150)
    type = models.PositiveSmallIntegerField(choices=Types.choices)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Action(models.Model):

    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=6, decimal_places=1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        suffix = 'km' if self.sport.type == 1 else ''
        return f'{self.sport.name} {self.value} {suffix}'