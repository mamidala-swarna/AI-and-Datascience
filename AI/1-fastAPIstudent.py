# GET -> Retrive data from the server(example: fetching user details from a database, get a list of products)

# POST -> send data to the server(example: creating a new user, submitting a form)

# PUT -> update existing data on the server(example: updating user profile information, changing a product's price)

# DELETE -> remove data from the server(example: deleting a user account, removing a product from the inventory)

# CRUD -> Create, Read, Update, Delete (the four basic operations for managing data in a database or application)

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Hello, World!'}

@app.get('/greet')
def greet():    
    return {'message': 'Hello, how are you doing?'}

@app.get('/students')
def get_students():
    students = [
        {'id': 1, 'name': 'Alice', 'age': 20},
        {'id': 2, 'name': 'Bob', 'age': 22},
        {'id': 3, 'name': 'Charlie', 'age': 21}
    ]
    return {'students': students}


students = [
        {'id': 1, 'name': 'Alice', 'age': 20},
        {'id': 2, 'name': 'Bob', 'age': 22},
        {'id': 3, 'name': 'Charlie', 'age': 21}
    ]
@app.get('/students/{student_id}')
def get_student(student_id: int):
    for student in students:
        if student['id']== student_id:
            return {'student': student} 
    return {'error': 'Student not found'}

# POST ->  creates records 

@app.post('/create_student')
def create_student():
    return {
        'message': 'Student created successfully'
    }

from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    age: int

@app.post('/create_student_with_data')
def create_student_with_data(student: Student):
    students.append(student.model_dump())
    return {
        'message': 'Student created successfully',
        'student': student
    }

