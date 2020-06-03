import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)
print(response)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

line_count = 1

for one_a_tag in soup.findAll('a'):
  # print(one_a_tag)
  if line_count >= 38:
    link = one_a_tag['href']
    download_url = 'http://web.mta.info/developers/' + link
    urllib.request.urlretrieve(download_url, './'+link[link.find('turnstile_')+1:])
    time.sleep(1)
  line_count += 1
# print(soup)