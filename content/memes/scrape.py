from lxml import html
import requests

import urllib2
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/libertarianmeme'

r_page = requests.get(url)
bs_page = urllib2.urlopen(url)
soup = BeautifulSoup(bs_page, 'html.parser')
name_box = soup.find('img', attrs={'class': 'media-element'})

# tree = html.fromstring(page.content)

# buyers = tree.xpath('//*[@id="t3_be8r2e"]/div[2]/div[3]/div/div[2]/a/div/div/img')
