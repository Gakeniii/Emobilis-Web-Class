from django.shortcuts import render, redirect
from Details.forms import RegistrationForm, Employee_details_form

# Create your views here.
def employees (request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form = RegistrationForm()
            return redirect('employees')
    else:
        form = RegistrationForm()
    return render(request, 'Employees.html', {'form': form})

def kin(request):
    if request.method == 'GET':
        form = Employee_details_form()
        return render(request, 'kins.html', {'form': form})
    else:
        form = Employee_details_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kins')
