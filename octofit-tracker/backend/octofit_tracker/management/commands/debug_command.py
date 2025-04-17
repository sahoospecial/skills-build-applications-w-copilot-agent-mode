from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Debug command to verify loading'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Debug command executed successfully!"))
