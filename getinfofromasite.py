from requests import get
from bs4 import BeautifulSoup
from json import dump
site='youtube.com'
def getinfofrom(site):
    res=get('http://'+site)
    print(res)
    soup=BeautifulSoup(res.text,'lxml')
    # print(soup.prettify())
    data={'name':site}
    print(soup.title.string)
    decryption=soup.find_all('meta',{'name':'description'})
    if len(decryption):
        print(decryption[0]['content'])
        data['description']=decryption[0]['content']
    kws=soup.find_all('meta',{'name':'keywords'})
    if len(kws):
        print(kws[0]['content'])
        data['keywords']=kws[0]['content']
    dump(data,open('./knw_sites/'+site,'w',encoding='utf8'))