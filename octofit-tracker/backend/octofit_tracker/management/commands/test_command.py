from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Test command to verify Command class loading'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Test command executed successfully.'))
