from django.shortcuts import render
import json
from .models import TrendTable

# Create your views here.
def homepage(request):
    return render(request, 'base.html')

def set_trends(request):
    data = request.GET
    min_ = sorted(data.items(), key=lambda kv: kv[1])[0][1]
    max_ = sorted(data.items(), key=lambda kv: kv[1])[-1][1]
    elements = [int(data[key]) for key in data]
    print(elements)
    mean = sum(elements) / len(elements)
    trends = TrendTable(
        slider_one=data['slider1'],
        slider_two=data['slider2'],
        slider_three=data['slider3'],
        slider_four=data['slider4'],
        slider_five=data['slider5'],
        lowest_value=min_,
        highest_value=max_,
        mean_value=mean
    )
    trends.save()
    return render(request, 'base.html')