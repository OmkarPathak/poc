from django.shortcuts import render
import json
from .models import TrendTable
from django.contrib import messages
import datetime

# Create your views here.
def homepage(request):
    return render(request, 'set_trends.html')

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
    messages.success(request, 'Entry added successfully!')
    return render(request, 'set_trends.html')

def get_datetime_object(date, format='%Y-%m-%d'):
    object = datetime.datetime.strptime(date, format).date()
    return object

def trends(request):
    if request.method == 'POST':
        to_date = request.POST.get('to_date')
        from_date = request.POST.get('from_date')

        # get all data
        result = TrendTable.objects.filter(
                    date_added__range=[
                                        get_datetime_object(to_date), 
                                        get_datetime_object(from_date) + datetime.timedelta(days=1)
                        ]
                    )
        
        # fetch only mean values from all entries
        results = []
        for res in result:
            date = int(res.date_added.strftime("%H"))
            results.append([date, res.slider_one])
            results.append([date, res.slider_two])
            results.append([date, res.slider_three])
            results.append([date, res.slider_four])
            results.append([date, res.slider_five])

        context = {
            'to_date': to_date,
            'from_date': from_date,
            'result': results
        }
        return render(request, 'trends.html', context=context)
    else:
        return render(request, 'trends.html')