numbers = [0, 1, 12, 33, 4, 15, 6, 27, 8, 90]
l=len(numbers)

for i in range(int(l/2)):
    print(i)
    n=numbers[i]
    numbers[i]=numbers[l-i-1]
    numbers[l-i-1]=n

print(numbers)
pass
#2nd way
#h=[]
#for i in numbers:
#    h.insert(0,i)
#    print(h)