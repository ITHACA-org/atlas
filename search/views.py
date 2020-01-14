from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

#from .forms import DateForm

import json
import requests

def index(request):
    #response = requests.get('https://catalogue.onda-dias.eu/dias-catalogue/Products?$search="name:*"&$top=3')
    #data = response.json()
    data = {}
    if 'name' in request.GET:
        name = request.GET['name']
        if 'startdate' in request.GET:
            end= request.GET['enddate']
            url = '"https://catalogue.onda-dias.eu/dias-catalogue/Products?$search=%22name:" \
                    +name+"  AND beginPosition:[" \
                    +start+"T00:00:00.000Z%20TO%20"+endsensingtime+"T00:00:00.000Z]%22"'
        url = 'https://catalogue.onda-dias.eu/dias-catalogue/Products?$search="name:%s "' %name
        print("ecco l'url finale" )
        print(url)
        response = requests.get(url)
        data = response.json()
    return render(request, 'search/index.html', {'data': data})




