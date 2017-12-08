import requests,re
from bs4 import BeautifulSoup
url='http://www.xiaohuar.com/list-1-0.html'
rp=requests.get(url)
rp.encoding='GBK'
html=rp.text
imgs=re.findall(r'src="(/d/file/\w+/\w+\.jpg)"',html)
for i in imgs:
    img='http://www.xiaohuar.com%s'%i
    imgname=i.split('/')[-1]
    file=requests.get(img).content
    with open (imgname,'wb') as f:
        f.write(file)
    print(img)
