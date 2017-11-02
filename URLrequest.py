import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
fhand = urllib.request.urlopen('https://www.taobao.com').read()

soup = BeautifulSoup(fhand,'html.parser')
tags=soup('a')
for tag in tags:
    print(tag.get('href',None))

