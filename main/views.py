from django.shortcuts import render
#from .models import Folstart 

def page(request):

    #dests = page.objects.all()

    return render(request, 'index.html')