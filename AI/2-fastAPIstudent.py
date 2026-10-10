from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample student data
students = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 22},
    {"id": 3, "name": "Charlie", "age": 21}
]


# Pydantic model for creating/updating a student
class Student(BaseModel):
    id: int
    name: str
    age: int


# Pydantic model for partial updates
class StudentPatch(BaseModel):
    name: str | None = None
    age: int | None = None


# GET: Retrieve all students
@app.get("/students")
def get_students():
    return {"students": students}


# GET: Retrieve one student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return {"student": student}

    return {"message": "Student not found"}


# POST: Create a new student
@app.post("/students")
def create_student(student: Student):
    if any(s["id"] == student.id for s in students):
        return {"message": "Student ID already exists"}

    new_student = student.model_dump()
    students.append(new_student)

    return {
        "message": "Student created successfully",
        "student": new_student
    }


# PUT: Completely update a student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for index, existing_student in enumerate(students):
        if existing_student["id"] == student_id:
            updated_student = student.model_dump()
            updated_student["id"] = student_id
            students[index] = updated_student

            return {
                "message": "Student updated successfully",
                "student": updated_student
            }

    return {"message": "Student not found"}


# PATCH: Partially update a student
@app.patch("/students/{student_id}")
def patch_student(student_id: int, student: StudentPatch):
    for existing_student in students:
        if existing_student["id"] == student_id:
            update_data = student.model_dump(exclude_unset=True)
            existing_student.update(update_data)

            return {
                "message": "Student updated successfully",
                "student": existing_student
            }

    return {"message": "Student not found"}


# DELETE: Remove a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, existing_student in enumerate(students):
        if existing_student["id"] == student_id:
            deleted_student = students.pop(index)

            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    return {"message": "Student not found"}
