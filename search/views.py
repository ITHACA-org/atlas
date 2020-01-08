from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

import json

def index(request):
    f = open('pippo.json')
    json_string = f.read()
    f.close()
    data = json.loads(json_string)
    #return HttpResponse("Ciao. Questa è la risposta.")
    #return HttpResponse(data)
    return render(request, 'search/index.html', data)
