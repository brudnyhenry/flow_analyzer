from django.conf.urls import url
from reports import views as reports_views


urlpatterns = [
        url(r'^customer$', reports_views.customer, name='reports_customer'),
        url(r'^history$', reports_views.history, name='reports_history'),
        ]