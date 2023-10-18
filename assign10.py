

# # single inheritance

class Teacher:
    school_name="viveka public school"
    def location(self):
        print("rentachintala")
class Student(Teacher):
    def __init__(self):
        self.name="venkat"
        self.cls="10th class"
    def show(self):
        print("name=",self.name)
        print("class=",self.cls)
        print("school=",self.school_name)
t=Student()
t.show()
t.location()

# # multilevel inheritance

class Owner:
    def Owner_work(self):
        print("owner told to servent to serve the order")
class Servent(Owner):
    def servet_work(self):
        print("servent asked customer to say the order")
class Customer(Servent):
    def customer_work(self):
        print("customer told the order to the servent")

c=Customer()
c.Owner_work()
c.servet_work()
c.customer_work()

# # hierarchical inheritance

class Company:
    def cview(self):
        print("company folder")
class Employee1(Company):
    def eview1(self):
        print("python folder")
class Employee2(Company):
    def eview2(self):
        print("java folder")
e1=Employee1()
e1.eview1()
e1.cview()
e2=Employee2()
e2.eview2()
e2.cview()


# multiple inheritance

class Father:
    def fmethod(self):
        print("this is your father")
class Mother:
    def mmethod(self):
        print("this is your mother")
class Child(Father,Mother):
    def cmethod(self):
        print("iam your child")
c=Child()
c.fmethod()
c.mmethod()
c.cmethod()
