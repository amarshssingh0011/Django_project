from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is the index page of myfirstapp.")

# Create your views here.
