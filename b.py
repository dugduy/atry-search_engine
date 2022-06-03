from requests import get
open('knew.txt','w',encoding='utf8').write('\n'.join([i['sentence'] for i in get('https://randomwordgenerator.com/json/sentences.json').json()['data']]))