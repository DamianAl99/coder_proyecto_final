from django.shortcuts import render
from django.http import HttpResponse
from services.models import Services
from services.forms import ServicesForm

# Create your views here.
def get_index(request):
    if 'search' in request.GET:
        search = request.GET['search']
        services = Services.objects.filter(name__icontains=search)
    else:
        services = Services.objects.all()
    context = {
        'services':services,
    }
    return render(request, 'index.html', context=context)

# def create_services(request):
#     if request.method == 'GET':
#         context = {
#                 'services': Services.objects.all(),
#                 'form': ServicesForm()
#         }
#         return render(request, 'services.html', context=context)

def get_data_from_DB(models, context_dicc):
    all_data = models.objects.all()
    return {
        context_dicc:all_data,
    }
