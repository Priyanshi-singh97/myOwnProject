my_list = [1, 2, 3, 4, 5,
           6, 7, 8, 9]
#hardcoded
#for i in range(9,0,-1):
#    j=i
#    print(j)

#dynamic
new_list=[]
for k in range((my_list.pop()),0,-1):
    l=k
    #print(l)
    new_list.append(l)
print(new_list)
