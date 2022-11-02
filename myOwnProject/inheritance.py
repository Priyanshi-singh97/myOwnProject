#class person(object):

#    def __init__(self, name, idNumber):

#        self.name=name
#        self.idNumber=idNumber

#    def display(self):
#        print(self.name)
#        print(self.idNumber)

#    def details(self):
#        print("my name is:".format(self.name))
#        print("Idnumber is:".format(self.idNumber))


#class child(person):
#    def __init__(self,name, idNumber,salary,post):

#        self.salary=salary
#        self.post=post
#        #since we are taking name & idnamuber fom theparent class so we have to invoke parent class here
#        person.__init__(self, name, idNumber)

#a=child('Rahul', 886012, 200000, "Intern")
#a.display()
#a.details()




class persone(object):
    def __init__(self,Namme,add):
        self.Namme=Namme
        self.add=add
        
    def display(self):
        print(self.Namme)
        print(self.add)
        
class child(persone):
    def __init__(self,Namme,add,no,id_no):
        self.no=no
        self.id_no=id_no
        persone.__init__(self,Namme,add)
        
c=child('Priya','lko',99,1)
c.display()

