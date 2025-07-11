#class creation 
class Person:
    # constructor 
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sayHello(self):
        print("Hello this is a class")
        print("Name is..",self.name)
        print("Age is..",self.age)
#create object 

person_1= Person("Srini",36)
person_1.sayHello()

    