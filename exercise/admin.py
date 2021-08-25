from django.contrib import admin

from .models import Sport
from .models import Action

admin.site.register(Sport)
admin.site.register(Action)
