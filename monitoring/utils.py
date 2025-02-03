import os
import platform
import socket

def ping_host(host):
    param = '-n 1' if platform.system().lower() == 'windows' else '-c 1'
    null = 'NUL' if platform.system().lower() == 'windows' else '/dev/null'
    command = f'ping {param} {host} > {null} 2>&1'
    response = os.system(command)
    return response == 0

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=3):
            return True
    except (socket.timeout, ConnectionRefusedError, socket.error):
        return False

def ping_and_check_service(hosts, port):
    results = {}
    for host in hosts:
        is_reachable = ping_host(host)
        is_service_active = check_port(host, port) if is_reachable else False
        results[host] = (is_reachable, is_service_active)
    return results