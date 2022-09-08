jo=[]
for i in range(11):
   if i==0:
    jo.append(i)
   if i>0:
        k=i-1
        a=jo.index(k)
        b=a-1
        jo.append(b)
print(jo)