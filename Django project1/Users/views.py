from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Index.html')

def aboutus(request):
    return render(request, 'Aboutus.html')

def contactus(request):
    return render(request, 'Contactus.html')

def login(request):
    return render(request, 'Login.html')

def register(request):
    return render(request, 'Register.html')



