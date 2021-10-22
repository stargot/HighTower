import requests
from django.core.management import BaseCommand
from ...models import Host


class Command(BaseCommand):
    """
    Check Hosts Django Management Command
    """
    def handle(self, *args, **kwargs):
        hosts = Host.objects.all()
        for host in hosts:
            r = requests.get(f'https://{host.host_name}')
            print(f'{host.host_name} {r.status_code}')
            if r.status_code == 200:
                host.status = True
            else:
                host.status = False
            host.save()
