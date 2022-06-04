from requests import get
from bs4 import BeautifulSoup
from json import dump
from threading import Thread
# site='youtube.com'
def getinfofrom(site):
    # print(site)
    res=get('http://'+site)
    # print(res)
    soup=BeautifulSoup(res.text,'lxml')
    # print(soup.prettify())
    data={'name':site}
    # print(soup.title.string)
    if soup.title:
        data['title']=soup.title.string
    decryption=soup.find_all('meta',{'name':'description'})
    if len(decryption):
        # print(decryption[0]['content'])
        data['description']=decryption[0]['content']
    kws=soup.find_all('meta',{'name':'keywords'})
    if len(kws):
        # print(kws[0]['content'])
        data['keywords']=kws[0]['content']
    dump(data,open('./knw_sites/'+site,'w',encoding='utf8'))
for i in open('./found.txt').read().splitlines():
    Thread(target=getinfofrom,args=(i,),daemon=1).start()
    # getinfofrom(i)