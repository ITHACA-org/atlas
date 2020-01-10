from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

import json
import requests

def index(request):
    #response = requests.get('https://catalogue.onda-dias.eu/dias-catalogue/Products?$search="name:*"&$top=3')
    #data = response.json()
    data = {}
    if 'name' in request.GET:
        name = request.GET['name']
        url = 'https://catalogue.onda-dias.eu/dias-catalogue/Products?$search="name:%s"' % name
        response = requests.get(url)
        data = response.json()
    return render(request, 'search/index.html', {'data': data})
