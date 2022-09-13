class person(object):

    def __init__(self, name, idNumber):

        self.name=name
        self.idNumber=idNumber

    def display(self):
        print(self.name)
        print(self.idNumber)

    def details(self):
        print("my name is:".format(self.name))
        print("Idnumber is:".format(self.idNumber))


class child(person):
    def __init__(self,name, idNumber,salary,post):

        self.salary=salary
        self.post=post
        #since we are taking name & idnamuber fom theparent class so we have to invoke parent class here
        person.__init__(self, name, idNumber)

a=child('Rahul', 886012, 200000, "Intern")
a.display()
a.details()
