from django . http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1> This is our demo page </h1>")
def chat(request):
    return HttpResponse("<h1> This is our chat page </h1>")
def about(request):
    return HttpResponse("<h1> This is our about page </h1>")
def setting(request):
    return HttpResponse("<h1> This is our setting page </h1>")
def search(request):
    return HttpResponse("<h1> This is our search page </h1>")


