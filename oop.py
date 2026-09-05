# Single Inheritance

class parent:
    def p(self):
        print("\n This is parent class method")

class child(parent):
    def p(self):
        print("This is child method")
    def c(self):
        self.p()
        super().p()
c1=child()
c1.c()

# Multiple Inheritance

class Parent1:
    def p1(self):
        print("Parent1")
class Parent2:
    def p2(self):
        print("Parent2")
class child(Parent1,Parent2):
    def c(self):
        print("Child")
        self.p1()
        self.p2()
c1=child()
c1.c()

# Multilevel Inheritance

class level1:
    def l1(self):
        print("level1")

class level2(level1):
    def l2(self):
        print("level2")
        self.l1()
class level3(level2):
    def l3(self):
        print("level3")
        self.l2()

l3=level3()
l3.l3()

# Hirarchical Inheritance

class parent:
    def p(self):
        print("Parent")
class child1(parent):
    def c1(self):
        print("Child1")
        self.p()
class child2(parent):
    def c2(self):
        print("Child2")
        self.p()
c=child1()
c1=child2()
c.c1()
c1.c2()

# Hybrid Inheritance

class grandparent:
    def gp(self):
        print("Grandparent")
class parent1(grandparent):
    def p(self):
        print("Parent1")
        self.gp()
class parent2:
    def p2(self):
        print("Parent2")
class child(parent1,parent2):
    def c(self):
        print("Child")
        self.p()
        self.p2()
c=child()
c.c()