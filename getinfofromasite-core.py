from requests import get
from bs4 import BeautifulSoup
site='youtube.com'
res=get('http://'+site)
print(res)
soup=BeautifulSoup(res.text,'lxml')
# print(soup.prettify())
print(soup.title.string)
decryption=soup.find_all('meta',{'name':'description'})
if len(decryption):
    print(decryption[0]['content'])
# print(soup.find_all('meta',{'name':'keywords'})[0]['content'])