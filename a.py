from time import sleep
f=open('./a.txt','a')
for i in range(10):
    print(i)
    sleep(1)
    f.write(str(i))