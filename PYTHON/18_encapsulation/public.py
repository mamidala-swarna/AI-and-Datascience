#public access
class A:
    def __init__(self,a):
        self.a=a # Public i.e No special naming conventions or prefixes 
obj=A(10)
print(obj.a)