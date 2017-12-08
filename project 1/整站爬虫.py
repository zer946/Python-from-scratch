import requests,re
for c in range(13):
    url='http://www.xiaohuar.com/list-1-%s.html'%c
    print (url)
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
    print ('.'*25,c,'.'*50)
