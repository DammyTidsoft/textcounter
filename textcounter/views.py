from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

# Create your views here.
def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'counter.html',{'amount':amount_of_words})
