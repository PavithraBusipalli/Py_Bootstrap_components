from django.shortcuts import render

# Create your views here.
def bootstrap_dwnldmethod(request):
    return render(request,'bootstrap_dwnldmethod.html')

def carousel1(request):
    return render(request,'carousel1.html')

def carousel_indicators(request):
    return render(request,'carousel_indicators.html')