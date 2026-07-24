#Method Overloading -Python doesn't support Traditional Method Overloading
#a=10
#a=20
#print(a)
class MathOps:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
obj=MathOps()
#obj.add(1,2)#TypeError: MathOps.add() missing 1 required positional argument: 'c'
print(obj.add(1,2,3))

print("=" * 50)

class MathOps:

    def add(self,*nums):
        return sum(nums)
    
obj=MathOps()
print(obj.add(1,2))
print(obj.add(1,2,3))
print(obj.add(1.5,2.5))