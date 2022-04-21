class Parent1:
    def __init__(self):
        self.tag = "Inside Parent Class-1"
    def show(self):
        print(self.tag)
          
class Parent2:
    def __init__(self):
        self.tag = "Inside Parent Class-2"
    def show(self):
        print(self.tag)
          
class Child(Parent1, Parent2):
    def __init__(self):
        self.tag = "Inside Child Class"
    def show(self):
        print(self.tag)
     
o1 = Child()
o2 = Parent2()
o1.show()
o2.show()