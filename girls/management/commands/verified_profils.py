from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from girls.models import Girls

class Command(BaseCommand):
    help = 'The command to write to the database  received from the core parser'

    def handle(self, *args, **options):
        users = Girls.objects.all()
        for user in users:

            response = requests.get(user.onlyfans_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            tag_a = soup.find('svg')
            if tag_a is not None:
                user.verified = True
                print(user.verified)
                user.save()

        self.stdout.write(self.style.SUCCESS('Comand Verified Success!!!'))