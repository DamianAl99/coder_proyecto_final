from django.shortcuts import render
from django.http import HttpResponse
from services.models import Services
from services.forms import ServicesForm

# Create your views here.
def get_services(request):
    context = get_data_from_DB(Services,"services")
    return render(request, 'services.html', context=context)

def create_services(request):
    print(request.method)
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            Services.objects.create(
                name=form.cleaned_data['name'],
                duration=form.cleaned_data['duration'],
                description=form.cleaned_data['description'],
            )
            form.clean()
            context = {
                'message': 'Servicio creado exitosamente',
                'services': Services.objects.all(),
                'form': ServicesForm()
            }
            return render(request, 'services.html', context=context)
        else:
            context = {
                'message': form.errors.as_text,
                'form': ServicesForm(),
                'services': Services.objects.all()
            }
            return render(request, 'services.html', context=context)
    if request.method == 'GET':
        context = {
                'services': Services.objects.all(),
                'form': ServicesForm()
        }
        return render(request, 'services.html', context=context)

def get_data_from_DB(models, context_dicc):
    all_data = models.objects.all()
    return {
        context_dicc:all_data,
    }