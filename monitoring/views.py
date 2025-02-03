from django.shortcuts import render
from django.http import JsonResponse
from .models import Host
from .utils import ping_and_check_service

def monitor_hosts(request):
    """View principal que renderiza a página de monitoramento."""
    return render(request, 'monitoring/monitor.html')

def fetch_host_data(request):
    """View que retorna os dados de monitoramento em formato JSON."""
    hosts = Host.objects.all()
    host_list = {host.name: (host.ip_address or host.name, host.flask_port) for host in hosts}
    results = {}

    for name, (ip, port) in host_list.items():
        ping_results = ping_and_check_service([ip], port)
        results[name] = {
            'ping_status': 'Online' if ping_results[ip][0] else 'Offline',
            'service_status': 'Rodando' if ping_results[ip][1] else 'Parado',
            'company': Host.objects.get(name=name).company,
            'os': Host.objects.get(name=name).operating_system
        }

    return JsonResponse({'results': results})
