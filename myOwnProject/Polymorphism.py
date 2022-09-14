#Polymorphism with Inheritance: 

class bird:

    def intro(self):
        print("there are many type og bird")

    def flight(self):
        print("most of them can fly and some can not fly")

class sparrow(bird):

    def flight(self):
        print("sprraow can fly")

class ostrich(bird):

    def flight(self):

        print("ostrich can not flight")

obj_bird = bird()
obj_spr = sparrow()
obj_ost = ostrich()


obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()

