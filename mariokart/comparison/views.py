from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("Hello, world. You're at the comparison home.")
    context = {}
    return render(request, 'home.html', context)
