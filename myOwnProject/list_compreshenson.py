#simple list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#newlist=[]
#try:
#    for i in fruits:
#        if "a" in i:
#            print(i)
#            newlist.append(i)
#except Exception as df:
#    []
#print(newlist)

#list comprehension
#newlist=[ i for i in fruits if "a" in i ]
# genrator exprsion
newlist=( i for i in fruits if "a" in i )

print (newlist)

