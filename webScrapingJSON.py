# Get movie info from Netflix
import requests
from bs4 import BeautifulSoup
import json

mid = '80121192'
url = 'https://www.netflix.com/watch/' + mid

response = requests.get(url)
page = response.content
soup = BeautifulSoup(page, "html.parser")

script = soup.find('script')
# print(script['type'])
# print(dir(script))

metadata = json.loads(script.text)
# print(metadata)

print(metadata['name'])
print(metadata['description'])

print()
print('Actors')
actors = metadata['actors']
for actor in actors:
    print(actor['name'])