from django.shortcuts import render
import json

# Create your views here.
def homepage(request):
    return render(request, 'base.html')

def set_trends(request):
    print(request.GET)
    data = json.loads(request.GET.copy())
    print(data)
    return render(request, 'base.html')