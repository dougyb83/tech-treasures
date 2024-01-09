from django.shortcuts import render

def index(request):
    """ returns the index page """
    return render(request, 'home/index.html')
