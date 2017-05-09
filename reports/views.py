import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from traffic.models import Client


@login_required
def customer(request):
    all_clients = Client.objects.all()
    current_year = datetime.datetime.now().year
    loop_range = range(2012, current_year + 1)

    # Check if it's a POST or GET request and return appropriate template
    if request.method == 'POST':
        client_pk = request.POST.get("customer_id", "")
        selected_year = request.POST.get("year", "")
        selected_month = request.POST.get("month", "")
        try:
            selected_client = Client.objects.get(pk=client_pk)
        except ValueError:
            print("You must select customer")
        try:
            traffic_for_client = selected_client.traffic_for_client.get(trafficTime='2017-04-01')
        except ValueError:
            print("You must select customer")

        # POST CONTEXT GENERATION

        context = {'context_customer_id': client_pk,
                   'context_year': selected_year,
                   'context_month': selected_month,
                   'context_all_clients': all_clients,
                   'context_traffic_for_client': traffic_for_client,
                   'context_loop_range': loop_range,
                   'context_selected_client': selected_client}

    # GET CONTEXT GENERATION
    else:
        context = {'context_all_clients': all_clients,
                   'context_loop_range': loop_range, }

    return render(request, 'reports/customer.html', context)


def history(request):
    return render(request, 'reports/history.html', context)

# Create your views here.
