# 1) Get page data
import requests 

url = 'https://en.wikipedia.org/'
response = requests.get(url)
page = response.content

# 2) Work with page data
from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'html.parser')
inTheNews = soup.find('div', id='mp-itn')

# 2.1) Print news text and links
news = inTheNews.find_all('li')
# for n in news:
#     print(n.get_text())
#     links = n.find_all('a')
#     for link in links:
#         print(link['href'])
#     print()

# 2.2) Save a picture
picDiv = inTheNews.find('div', class_='itn-img')
picture = picDiv.find('img')
src = picture['src']
# print(src)
r = requests.get('https:' + src)
fName = src[src.rfind('/') + 1 : ].replace('%','')
# print(fName)

open(fName, 'wb').write(r.content)
