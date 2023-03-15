from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from girls.models import Girls

def get_urls_links():
    urls_links = set([])
    nexts_pages = []
    url_trend = 'https://fapello.com/random/'
    while len(urls_links) < 50:
        response_trend = requests.get(url_trend)
        soup = BeautifulSoup(response_trend.content, 'html.parser')
        content_div = soup.find('div', id='content')
        a_tags = content_div.find_all('a', class_=False)
        for a in a_tags:
            url_a = a['href']
            urls_links.add(url_a)
            if len(urls_links) == 50:
                break

        div_page = soup.find('div', id='next_page')
        next_page = div_page.a['href']
        nexts_pages.append(next_page)
        url_trend = next_page
    print(len(urls_links), "LENS LINKS")
    return list(urls_links)

def get_user_links():
    urls_links = get_urls_links()
    urls_users = []
    for url in urls_links:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        div_elem = soup.find('div', class_='flex flex-1 items-center space-x-4')
        urls_users.append(div_elem.a['href'])
    print(len(urls_users), "USER URLS")
    return urls_users

class Command(BaseCommand):
    help = 'The command to write to the database dvushek received from the core parser'

    def handle(self, *args, **options):

        urls = get_user_links()
        users_names = []
        for url in urls:
            response = requests.get(url)
            print(response)
            soup = BeautifulSoup(response.content, 'html.parser')
            user_name = soup.find('p')
            p_url_fans = user_name.find_next('p')
            if p_url_fans is not None and p_url_fans.a is not None \
                    and p_url_fans.a['href'].startswith('https://onlyfans.com/'):

                user_url_fans = p_url_fans.a['href']
                if ',' in user_name.text:
                    first_name = user_name.text.split(',')[0].strip()
                    users_names.append({'username':first_name,'onlyfans': user_url_fans})
                else:
                    user_url_fans = p_url_fans.a['href']
                    users_names.append({'username':user_name.text,'onlyfans': user_url_fans})

        for girl in users_names:

            girl, created = Girls.objects.get_or_create(user_name=girl['username'], onlyfans_url=girl['onlyfans'])

        self.stdout.write(self.style.SUCCESS('Comand add to datebase Success!!!'))



