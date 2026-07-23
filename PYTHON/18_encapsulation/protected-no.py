# Private Access 

class A:
    def __init__(self,a):
        self.__a = a # Private i.e special naming conventions __var 

obj = A(10)

# print(obj.a) # AttributeError: 'A' object has no attribute 'a'

class B(A):
    def showA(self):
        a = A(10)
        print(a.__a)
        
obj = B(20)
obj.showA()        