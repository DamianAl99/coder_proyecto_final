from django.shortcuts import render
from django.http import HttpResponse
from schedules.models import Schedules
from schedules.forms import SchedulesForm

# Create your views here.
def get_schedules(request):
    context = get_data_from_DB(Schedules,"Schedules")
    return render(request, 'schedules.html', context=context)

def create_schedules(request):
    if request.method == 'POST':
        form = SchedulesForm(request.POST)
        if form.is_valid():
            Schedules.objects.create(
                cliente=form.cleaned_data['cliente'],
                services=form.cleaned_data['services']
            )
            form.clean()
            context = {
                'message': 'Agendado/a exitosamente',
                'schedules': Schedules.objects.all(),
                'form': SchedulesForm()
            }
            return render(request, 'schedules.html', context=context)
        else:
            context = {
                'message': form.errors.as_text,
                'form': SchedulesForm(),
                'schedules': Schedules.objects.all()
            }
            return render(request, 'schedules.html', context=context)
    if request.method == 'GET':
        context = {
                'schedules': Schedules.objects.all(),
                'form': SchedulesForm()
        }
        return render(request, 'schedules.html', context=context)

def get_data_from_DB(models, context_dicc):
    all_data = models.objects.all()
    return {
        context_dicc:all_data,
    }