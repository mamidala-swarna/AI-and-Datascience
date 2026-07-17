#Exception Handling
#when there is no errors ->nothing to handle
print("Program Execution Started")
num1=10
num2=5
print("Result: ",num1/num2)
print("Program Execution Completed")

print("=" * 50)

##When Errors->abruptly "STOPS" the program execution
#print("Program Execution Started")
#num1=10
#num1="5"
#print("Result: ",num1/num2)#TypeError: unsupported operand type(s) for /: 'str' and 'int'
#print("Program Execution Completed ")

#print("=" * 50)

#When errors --> Developers Handling Exceptions
print("Program Execution Started")
num1=10
num2="5"
try:
    print("Result: ",num1/num2)
except:
    print("WARNING! Don't Divide Numbers With Strings")

print("=" * 50)

#When No Errors ->Developers Handling Exceptions

print("Program Execution Started")
num1=10
num2=5
try:
    print("Result: ",num1/num2)
except:
    print("WARNING ! Don't Divide Numbers with Strings")
print("Program Execution Completed")

print("=" * 50)

# When Errors --> Python Handling Exceptions 
# print("Program Execution Started")

# num1 = 10
# num2 = 0

# print("Result: ", num1/num2) # ZeroDivisionError: division by zero

# print("WARNING! Don't Divide Numbers With Strings")

# print("Program Execution Completed")

# print("=" * 50)

# When Errors --> Developers Handling Exceptions 

print("Program Execution Started")
num1=10
num2=0
try:
    print("Result: ",num1/num2)
except:
    print("WARNING! Don't Divide Numbers with Zero")
print("Program Execution Completed")

print("=" * 50)

#When Multiple Errors Occur
#data=[1,2,'three',0,4]
#data=[1,2,0,4]
data=[1,2,4]
for num in data:
    print(1/num)

print("=" * 50)

# When Multiple Errors Occur  --> Developers Handling Exceptions 
print("Program Execution Started")
data=[1,2,'three',0,4]
for num in data:
    try:
        print(1/num)
    except:
        print("OOPS!!! Something Went Wrong")
print("Program Execution Completed")

print("=" * 50)

# When Multiple Errors Occur Use Multiple except blocks  --> Developers Handling Exceptions 
print("Program Execution Started")
data=[1,2,'three',0,4]
for num in data:
    try:
        print(1/num)
    except TypeError:
        print("OOPS!!! Don't divide numbers with strings")
    except ZeroDivisionError:
        print("OOPS!! Don't divide numbers with zero")

print("Program Execution Completed")
print("=" * 50)

# When Errors occur else scenario --> Developers Handling Exceptions
print("Program Execution Started")
num1=10
num2=5
try:
    print("Result: ",num1/num2)# Verify Login Credentials 
except:
    print("WARNING! Don't divide numbers with Zero")
else:
    print("Calculation Was Successful")# Then Only check for OTP
print("Program Execution Completed")
print("=" * 50)

# When Errors occur finally scenario --> Developers Handling Exceptions 
print("Program Execution Started")
num1 = 10
num2 = 5
try:
    print("Result: ", num1/num2) # Verify Login Credentials 
except:
    print("WARNING! Don't divide numbers with zero")
else:
    print("Calculation Was Successful")
finally:
    print("Closing all database connections and file streams")
print("Program Execution Completed")
print("=" * 50)

# When Errors occur finally scenario --> Developers Handling Exceptions 
print("Program Execution Started")
num1 = 10
num2 = 0
try:
    print("Result: ", num1/num2) # Verify Login Credentials 
except:
    print("WARNING! Don't divide numbers with zero")
else:
    print("Calculation Was Successful")
finally:
    print("Closing all database connections and file streams")
print("Program Execution Completed")
print("=" * 50)

#Cuatom Exceptions
age=int(input("Enter a Age: "))
if age <18:
    print("You cannot Vote")
else:
    print("You can vote")
print("=" * 50)

#Custom Exceptions Specific to your program
#class UnderAgeError(Exception):
 #pass
#ge=int(input("Enter a Age: "))
#if age < 18:
 #   print("You cannot vote")
  #  raise UnderAgeError
#else:
 #   print("You can vote")
#print("=" * 50)

#Custom Exceptions Specific to your program
#class UnderAgeError(Exception):
 #pass
#age=int(input("Enter a Age: "))
#if age < 18:
  #  print("You cannot vote")
 #   raise UnderAgeError("Below 18 cannot vote")
#else:
 #   print("You can vote")
#print("=" * 50)

#Custom Exceptions Specifif to your program
class UnderAgeError(Exception):
    pass
age=int(input("Enter a Age: "))
try:
    if age < 18:
        raise UnderAgeError("Below 18 cannot Vote")
except UnderAgeError:
    print("You are not 18 yet !!!!")
else:
    print("You can vote")
print("=" * 50)
    