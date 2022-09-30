a=[123,478,921]
b=[]
#[6,19,12]

for i in a:
    stf=0
    for j in str(i):
        stf+=int(j)
    b.append(stf)
print(b)



