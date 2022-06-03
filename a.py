knowlist=open('knew.txt',encoding='utf8').read().splitlines()
def mysearch(kw):
    result=[]
    for i in knowlist:
        if kw.lower().strip() in i.lower():
            result.append(i)
    return result
kw=input('Search: ')
result=mysearch(kw)
print(len(result),'for',kw)
for i in result:
    print(i.replace(kw,'|%s|'%kw))