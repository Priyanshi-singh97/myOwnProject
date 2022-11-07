#class student:
#    def __init__(self,firstname,lastname):
#        self.firstname=firstname
#        self.lastname=lastname
        
#obj=student('p','s')
#print(obj.firstname)
#print(obj.lastname)



#a=[20,6,8,3,9,11]
#c=[]
#for i in a:
#    for j in range(2,i):
#       if i==j:
#           print(i)
#       elif i%j==0:
#           pass
#       elif i%j!=0:
#           c.append(j)
#       else:
#            print(i)

class student:
    def __init__(self,fist,last):
        self.fist=fist
        self.last=last
        
    #def display(self):
    #    print(self.fist)
    #    print(self.last)
p1=student('p','s')
print(p1.fist)
print(p1.last)