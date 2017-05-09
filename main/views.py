from django.shortcuts import render
from traffic.models import Client


def home(request):
    all_clients = Client.objects.all()

    top_traffic = {}
    for x in all_clients:
        top_traffic[x] = x.traffic_for_client.get(trafficTime='2017-04-01')
    context = {'top_traffic': top_traffic}

    return render(request, "main/home_2.html", context)

# Create your views here.
