from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import AdmissionForm

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

class HelloPakistan(View):
    def get(self, request):
        return HttpResponse("Hello Pakistanis")

def home(request):
    form = AdmissionForm()

    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Admission successful")

    return render(request, 'index.html', {'form': form})

