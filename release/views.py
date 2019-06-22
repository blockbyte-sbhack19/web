from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("release view")

def detail(request, soil_id):
    return HttpResponse("You're looking at soil %s." % soil_id)

def history(request, soil_id):
    response = "You're looking at the history of soil %s."
    return HttpResponse(response % soil_id)

def vote(request, soil_id):
    return HttpResponse("You're submitting on soil %s." % soil_id)