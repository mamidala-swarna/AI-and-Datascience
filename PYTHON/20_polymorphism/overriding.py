#Method Overriding-provides a new implementation of a method that already exists in parent class
class Animal:

    def sound(self):
        print("An Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog makes sound- Woof")

class Cat(Animal):
    def sound(self):
        print("Cat makes sound-Meow")

animal=Animal()
animal.sound()

dog=Dog()
dog.sound()

cat=Cat()
cat.sound()

