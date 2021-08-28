from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Action
from .models import Sport
from .forms import ActionForm

def index(request):
    actions = Action.objects.order_by('-date')[:30]
    sports = Sport.objects.only('id', 'name')
    action_form = ActionForm()

    context = {
        'actions': actions,
        'sports': sports,
        'action_form': action_form
    }
    return render(request, 'exercise/index.html', context)

def add(request):

    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.save()

    return HttpResponseRedirect('/exercise')

