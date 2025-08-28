from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm  # Import the ReservationForm


# Create your views here.
def hello_world(request):
    return HttpResponse("HELlo wWorld")


class HelloWorls(View):

    def get(self,request):
        return HttpResponse("Heloo World class")


def home(request):
    
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation created successfully!")
        
    return render(request, 'index.html', {'form': form})