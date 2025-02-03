from django.urls import path
from .views import monitor_hosts, fetch_host_data

urlpatterns = [
    path('monitor/', monitor_hosts, name='monitor_hosts'),
    path('monitor/data/', fetch_host_data, name='fetch_host_data'),
]
