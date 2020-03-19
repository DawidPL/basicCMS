from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help='db migrations and runserver'

    def handle(self, *args, **kwargs):
        for option in ['makemigrations', 'migrate', 
                        'createsuperuser', 'collectstatic','runserver']:
            try:
                call_command(option)
                self.stdout.write(self.style.SUCCESS(f'********** Command {option} has been execute without any error **********'))
            except:
                self.stdout.write(self.style.NOTICE(f'********** Command {option} does not exist ! **********'))


