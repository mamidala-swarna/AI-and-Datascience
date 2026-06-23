#Arithmetic operations
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

#Profile Related Information
institute="Digital Edify"
maintainer="developer@digital.com"

def profile():
    return f"Welcome To {institute} - You are using Module Developed By {maintainer}"
    
answer=profile() 
print(answer)