from django.shortcuts import render
from myapp.models import Car

# Create your views here.
def index(request):
    car = Car.objects.all()
    return render(request, 'index.htm', {'car': car})
