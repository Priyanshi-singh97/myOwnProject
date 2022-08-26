arr=[1,2,3,4,5,6,7,8,9]
k=3
arr1=[]


for i in range(0,12,k):
    x=i
    aa1=arr[x:x+k]
    print(aa1)
    if (i==0 or i==3 or i==6):
        i1=aa1[-1]
        arr1.append(i1)
        i2=aa1[-2]
        arr1.append(i2)
        i3=aa1[-3]
        arr1.append(i3)
print(arr1)