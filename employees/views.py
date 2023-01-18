from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employees
from employees.forms import EmployeesForm

# Create your views here.
def get_clientes(request):
    context = get_data_from_DB(Employees,"employees")
    return render(request, 'employees.html', context=context)

def create_clients(request):
    if request.method == 'POST':
        try:
            form = EmployeesForm(request.POST)
            if form.is_valid():
                Employees.objects.create(
                    name=form.cleaned_data['name'],
                    age=form.cleaned_data['age'],
                    ci=form.cleaned_data['ci'],
                )
                form.clean()
                context = {
                    'message': 'Empleado creado exitosamente',
                    'employees': Employees.objects.all(),
                    'form': EmployeesForm()
                }
                return render(request, 'employees.html', context=context)
            else:
                context = {
                    'message': form.errors,
                    'form': EmployeesForm(),
                    'employees': Employees.objects.all()
                }
                return render(request, 'employees.html', context=context)
        except:
            context = {
                    'message': "hubo un error al crear el cliente",
                    'form': EmployeesForm(),
                    'employees': Employees.objects.all()
                }
            return render(request, 'employees.html', context=context)

    if request.method == 'GET':
        context = {
                'employees': Employees.objects.all(),
                'form': EmployeesForm()
        }
        return render(request, 'employees.html', context=context)

def get_data_from_DB(models, context_dicc):
    all_data = models.objects.all()
    return {
        context_dicc:all_data,
    }