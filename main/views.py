from django.shortcuts import render

# Create your views here.
def summarypage(request):
    return render (request, 'main/summarypage.html')

def intropage(request):
    return render (request, 'main/intropage.html')