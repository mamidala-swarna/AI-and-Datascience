#Types of Inheritance
#without Inheritance
class Father:
    def house(self):
        print("Has House")
class Son:
    def car(self):
        print("Has Car")
son_object=Son()
son_object.car()
#son_object.house()#attribute error->'son' object has no attributr'house'
print("=" * 50)

#with Inheritance
class Father:
    def house(self):
        print("Has House")
class Son(Father):# Single Level Inheritance
    def car(self):
        print("Has Car")

son_object=Son()
son_object.car()
son_object.house()

print("=" * 50)
# Multi Level Inheritance:= |GrandParent -> Parent -> Child|
class GrandFather:
    def land(self):
        print("Has Land")
class Father(GrandFather):
    def house(self):
        print("Has House")
class Son(Father):# Multi Level Inheritance
    def car(self):
        print("Has Car")

son_object=Son()
son_object.car()
son_object.house()
son_object.land()

print("=" * 50)
# Multiple Inheritance: Father | Mother 
#                            Child

class GrandFather:
    def land(self):
        print("Has Land")
        
class Father(GrandFather):
    def house(self):
        print("Has House")
        
class Mother:
    def gold(self):
        print("Has Gold")

class Son(Father,Mother):# Multiple Level Inheritance
    def car(self):
        print("Has Car")
son_object = Son()
son_object.car()
son_object.house()
son_object.land()
son_object.gold()

print("=" * 50)

#                             Parent
# Hierarchical Inheritance: Son | Daughter 
# One Parent -> Multiple Child  

class GrandFather:
    def land(self):
        print("Has Land")

class Father(GrandFather):
    def house(self):
        print("Has House")
class Mother:
    def gold(self):
        print("Has Gold")
class Son(Father):
    def car(self):
        print("Has Car")
class Daughter(Father):
    def business(self):
        print("Has Busines")

son_object=Son()
son_object.car()
son_object.house()
son_object.land()

daughter_object=Daughter()
daughter_object.business()
daughter_object.house()
daughter_object.land()

print("=" * 50)

# Hybrid Inheritance: Combination Of Types Of Inheritance
class A:
    def a(self):
        print("A")
class B(A):
    def b(self):
        print("B")
class C(A):
    def c(self):
        print("C")
class D(B,C):
    def d(self):
        print("D")
object_d=D()
object_d.a()
object_d.b()
object_d.c()
object_d.d()