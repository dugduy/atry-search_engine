from itertools import product
from requests import get
from threading import Thread
tlds=open('./all_tld.txt').read().splitlines()
mystr='abcdefghijklmnopqrstuvwxyz1234567890'
def checkadm(dm):
    try:
        res=get(dm)
        print(dm,'found!')
        open('found.txt','a').write(dm+'\n')
    except:
        print(dm,'is not exist!')
for i in range(1,5):
    for j in product(mystr,repeat=i):
        for tld in tlds:
            crdm='http://'+''.join(j)+'.'+tld
            Thread(target=checkadm,args=(crdm,)).start()