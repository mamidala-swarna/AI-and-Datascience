# OOP - Object Oriented Programming 

# Class - Blue Print 

class Student:
#Students has Something-characteristics/properties(VARIABLES)
 student_name="Swarna"
 student_email="swarnamamidala@gmail.com"


# Student Does Something - Behaviors / Actions (METHODS)
def student_studies():
    print("Student is Studying Python")

#To use this class,object is required
student_object=Student()

print("Student Name:",student_object.student_name)
print("Student Email:",student_object.student_email)

print("=" * 50)

# Class - Blue Print 

class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "kirthana"
    student_email = "kirthana@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        
# To Use this class, object is required 
student_object = Student()

print("Student Name: ",student_object.student_name)
print("Student Email: ",student_object.student_email)

student_object.student_studies() 

print("=" * 50)
# Class - Blue Print 

class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "vighnesh"
    student_email = "vighnesh@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",student_object.student_email) # Not Recommended
        
# To Use this class, object is required 
student_object = Student()

student_object.student_studies() 

print("=" * 50)
# Class - Blue Print 

class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "ananya"
    student_email = "ananya@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Not Recommended
        
# To Use this class, object is required 
student_object = Student()

student_object.student_studies() 

print("=" * 50)

# Working With Multiple Objects 

class Student:
    
    # Student Has Something - Characteristics / Properties (VARIABLES)
    student_name = "varsha"
    student_email = "varsha@gmail.com"
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Not Recommended
# To Use this class, object is required 
student_varsha= Student()
student_varsha.student_studies() 

student_john = Student()
student_john.student_studies() 

student_mike = Student()
student_mike.student_studies() 

print("=" * 50)
# Working With Multiple Objects Using Constructor i.e __init__() method

class Student:
      # Constructor i.e __init__() method
    def __init__(self,student_name,student_email):
        print("Constructor Called")
        self.student_name = student_name
        self.student_email = student_email
        
    
    # Student Does Something - Behaviors / Actions (METHODS)
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Not Recommended
        
# To Use this class, object is required 
# student_ravi = Student()
student_sunny = Student("sunny","sunny@gmail.com")
student_sunny.student_studies() 

student_john = Student("john","john@gmail.com")
student_john.student_studies() 

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies() 

print("=" * 50)

# Working With Instance Members 
class Student:
    
    # Constructor i.e __init__() method
    def __init__(self,student_name,student_email):
        print("Constructor Called")
        # Instance Variables self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
        
    
    # Student Does Something - Behaviors / Actions (METHODS)
    # Instance Method is student_studies()
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Not Recommended
        
# To Use this class, object is required 
# student_ravi = Student()
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies() 

student_john = Student("john","john@gmail.com")
student_john.student_studies() 

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies() 

print("=" * 50)

# Working With Class Members 
class Student:
    
    # Class Variable - "shared by all the objects"
    institute_name = "Digital Institute"
    
    # Constructor i.e __init__() method
    def __init__(self,student_name,student_email):
        print("Constructor Called")
        # Instance Variables self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
        
    
    # Student Does Something - Behaviors / Actions (METHODS)
    # Instance Method is student_studies()
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        print("At Institute: ",self.institute_name) # Not Recommended
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Recommended
        print("At Institute: ",Student.institute_name) # Recommended
        
    # Class Method 
    @classmethod
    def change_institute_name(cls,new_institute_name):
        cls.institute_name = new_institute_name
        # Accessing instance data inside a class method gives error 
        # print("Student Name: ",self.student_name) # NameError: name 'self' is not defined
        
        
# To Use this class, object is required 
# student_ravi = Student()
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies() 

student_john = Student("john","john@gmail.com")
student_john.student_studies() 

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies() 

# Class Method 
Student.change_institute_name("New Institute")

student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies() 

student_john = Student("john","john@gmail.com")
student_john.student_studies() 

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies() 


print("=" * 50)

# Working With Static Members 
class Student:
    
    # Class Variable - "shared by all the objects"
    institute_name = "Digital Institute"
    
    # Constructor i.e __init__() method
    def __init__(self,student_name,student_email):
        print("Constructor Called")
        # Instance Variables self.student_name & self.student_email
        self.student_name = student_name
        self.student_email = student_email
        
    
    # Student Does Something - Behaviors / Actions (METHODS)
    # Instance Method is student_studies()
    def student_studies(self): # passed "self" nothing but object reference 
        print("Student Is Studying Python")
        print("At Institute: ",self.institute_name) # Not Recommended
        print("Student Name: ",self.student_name) # Recommended
        print("Student Email: ",self.student_email) # Recommended
        print("At Institute: ",Student.institute_name) # Recommended
        
    # Class Method 
    @classmethod
    def change_institute_name(cls,new_institute_name):
        cls.institute_name = new_institute_name
        # Accessing instance data inside a class method gives error 
        # print("Student Name: ",self.student_name) # NameError: name 'self' is not defined
    
    # Static Method 
    @staticmethod
    def something_not_related_to_class_object(a,b):
        print("I Do Something that is not associated with Classes & Objects")
        print("Sum Of Numbers: ",(a+b))
        
        
# To Use this class, object is required 
# student_ravi = Student()
student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies() 

student_john = Student("john","john@gmail.com")
student_john.student_studies() 

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies() 

# Class Method 
Student.change_institute_name("New Institute")

student_ravi = Student("ravi","ravi@gmail.com")
student_ravi.student_studies() 

student_john = Student("john","john@gmail.com")
student_john.student_studies() 

student_mike = Student("mike","mike@gmail.com")
student_mike.student_studies() 


# Static Method
Student.something_not_related_to_class_object(10,10)

print("=" * 50)
