#import re
#xml_string="""<?xml version="1.0" encoding="UTF-8"?> <note> <to>Tove</to> <from>Jani</from> <heading>Reminder</heading> <body> </body> </note> """
#xml_string1=xml_string.replace('<?xml version="1.0" encoding="UTF-8"?>',' ')
#xml_string2=xml_string.replace('<body> </body>','<body> Hi priya </body>')

#print(xml_string2)

#a=[[1,1]]
#b=a+a
##[[1,1],[1,1]]
#c=b[0][0]+99
#b[0][0]=100
#print(b)

#d=[[1,2],[3,4]]
#d[0][0]=100
#print(d)

#import pandas as pd
#animal = 'cat dog cat fish dog cat cat' 
#size = 'SSMMMLL' 
#weight = [8, 10, 11, 1, 20, 12, 12] 
#adult = [False, False, False, False, False, True, True]

#k=pd.DataFrame(animal)
#print(k)


#df = pd.DataFrame( {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]} )
#if df['AAA'].all()>=6:
#    df['BBB']==-1
#    print(df)


#s='abbbccccda'

#v=''
#count=0
###op='1a2b4c1d1a'
#for i in s:
#    if i in s:
#        count=count+1
#        k=str(count)
#        v+=(k+ i)
#        #'+str(Today_date)+'
       
#print(v)



#a = [10, 3.3, 4.6, 3.3, 3.5, 6.1, 7.1, 7, 2]

##Out[5]: {2: 1, 3.3: 2, 3.5: 3, 4.6: 4, 6.1: 5, 7: 6, 7.1: 7, 10: 8
#l=len(a)
#k=sorted(a)
#l={i:idx  for idx, i in enumerate(k)}
#print(l)

A= [1,2,3,5]
k=len(A)
l=[]
for i in A:
    f=k+1
    for j in range(1,f):
       if i==j:
           l.append(i)
           break
       else:
           print(j)
        




