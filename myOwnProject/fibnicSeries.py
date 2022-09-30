n=[1,5,2,4,6,7,9]
n1=[]
#make this list into fibonic series
for i in range(len(n)):
    if i<=1:
        n1.append(i)
    else:
        n2=(i-1)+ (i-2)
        n1.append(n2)

print(n1)

