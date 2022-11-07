#import re
#xml_string="""<?xml version="1.0" encoding="UTF-8"?> <note> <to>Tove</to> <from>Jani</from> <heading>Reminder</heading> <body> </body> </note> """
#xml_string1=xml_string.replace('<?xml version="1.0" encoding="UTF-8"?>',' ')
#xml_string2=xml_string.replace('<body> </body>','<body> Hi priya </body>')

#print(xml_string2)

a=[[1,1]]
b=a+a
#[[1,1],[1,1]]
c=b[0][0]+99
b[0][0]=100
print(b)

d=[[1,2],[3,4]]
d[0][0]=100
print(d)

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


s='abbccccda'

v=''
count=0
#op='1a2b4c1d1a'
for i in s:
    count(s[i])

print(v)



#a = [10, 3.3, 4.6, 3.3, 3.5, 6.1, 7.1, 7, 2]
#a=[]
##Out[5]: {2: 1, 3.3: 2, 3.5: 3, 4.6: 4, 6.1: 5, 7: 6, 7.1: 7, 10: 8
#l=len(a)
#k=sorted(a)
#for i in range(len(k)):
#   c= k[i] +':'+ l-i
#   a.append(c)

#print(a)