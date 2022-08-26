arr=[1,2,3,7,5]
sum = 0
arr1=[]
for i in range(len(arr)):
    try:
        k=arr[i]
        j=arr[i+1]

        kj=k+j
    except Exception as bf:
        pass
    finally:
        arr.append(kj)
print(arr)

#for i in range(0,len(arr)):
#    sum = sum + arr[i]
#    print(sum)