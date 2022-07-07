from django.shortcuts import render
import requests


# Create your views here.

def home(request):
    concept_name=request.GET.get('concept_name')
    if request.method == 'GET':
        if concept_name is None:
            endpoint="http://127.0.0.1:8000/api/concepts/"
            get_response=requests.get(endpoint)
            context={'data': get_response.json()}
            return render(request,'base/home.html',context)
        else:
            print("searching")
            endpoint=f"http://127.0.0.1:8000/api/concepts/search?concept_name={concept_name}"
            get_response=requests.get(endpoint)
            context={'data': get_response.json()}
            return render(request,'base/home.html',context)
    elif request.method =='POST':
        concept_id__in=request.POST.getlist('concept_id__in')
        endpoint="http://127.0.0.1:8000/api/concepts/filter?concept_id__in="
        endpoint+=concept_id__in[0]
        for i in range(1,len(concept_id__in)):
            endpoint+=','+concept_id__in[i]
        get_response=requests.get(endpoint)
        context={'data': get_response.json()}
        return render(request,'base/filtered_data.html',context)
