from django.shortcuts import render, redirect
from Home.forms import RegisterForm, RegistrationForm, ProfileForm
from django.contrib import messages


# Create your views here.
def index(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form = RegistrationForm()        # helps refresh the form after use
            messages.success(request, 'User registered successfully!')
            return redirect('index')   # show where you want the message to appear from
    else:
        form = RegistrationForm()
    return render(request, 'Index.html', {'form': form})

def about(request):
    # form = StudentComplains()
    return render(request, 'About.html')   # {'form': form})

def contact(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProfileForm()
            messages.success(request, 'Data input was successful!')
            return redirect('contact')
    else:
        form = ProfileForm()
    return render(request, 'Contact.html', {'form': form})   # {'form': form})

def gallery(request):
    return render(request, 'Gallery.html')

