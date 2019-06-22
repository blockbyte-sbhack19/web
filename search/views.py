from django.http import HttpResponse
from django.template import loader

from .models import Soil

def index(request):
    latest_soil_list = Soil.objects.order_by('-beforeDate')[:5]
    template = loader.get_template('issue/index.html')
    context = {
        'latest_soil_list': latest_soil_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, soil_id):
    return HttpResponse("You're looking at soil %s." % soil_id)

def history(request, soil_id):
    response = "You're looking at the history of soil %s."
    return HttpResponse(response % soil_id)

def vote(request, soil_id):
    return HttpResponse("You're submitting on soil %s." % soil_id)