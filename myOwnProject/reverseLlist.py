#arr=[1,2,3,4,5,6,7,8,9]
#k=3
#arr1=[]


#for i in range(0,12,k):
#    x=i
#    aa1=arr[x:x+k]
#    print(aa1)
#    if (i==0 or i==3 or i==6):
#        i1=aa1[-1]
#        arr1.append(i1)
#        i2=aa1[-2]
#        arr1.append(i2)
#        i3=aa1[-3]
#        arr1.append(i3)
#print(arr1)



#N = 5, K = 3
#arr[] = {1,2,3,4,5}
#Output: 3 2 1 5 4

#def rev(arr):
    
#    k=input()
#    x=range(len(arr),k)
#    for i in x:
        
#        print(i)
        
#rev([1,2,3,4,5])
        
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n=3
sub_list = [l[i:i+ n] for i in range(0,len(l),n)]
#reverse_list=[j[::-1] for j in sub_list]
reverse_list=[(j.pop()) for j in sub_list]
print(reverse_list)

