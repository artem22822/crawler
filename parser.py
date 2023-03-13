import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from xml.etree.ElementTree import ElementTree, Element

API_KEY = '4a0f43c0-a592-463e-8f87-402312f353a0'

def get_scrapeops_url(url):
            payload = {'api_key': API_KEY, 'url': url, 'bypass': 'cloudflare'}
            proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
            return proxy_url

response = ElementTree()
response.parse('fansmetrics.xml')

root = response.getroot()
elements = root.findall('./url')

urls = []
for i in range(5):
    element = elements[i]
    loc = element.find('loc').text
    urls.append(loc)

users_names = []
users_imgs = []
for url in urls:
    print(url)
    response_1 = requests.get(get_scrapeops_url(url))
    soup = BeautifulSoup(response_1.content,'html.parser')
    user_name = soup.h3.string
    users_names.append(user_name)
    user_img = soup.find('img')
    users_imgs.append(user_img['src'])


