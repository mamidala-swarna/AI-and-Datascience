# Student Management System -> Using Functional Style 

# Menu Based System -> In Future if you learn html, css, js etc, replace menus with 
# UI Elements like Buttons 

# System Setup -> READ ONLY (Tuple)
# System_info = () # Not Recommended 
SYSTEM_INFO = ("Digital Edify","Student Management System","v1")

# Admin Info -> READ ONLY (Tuple)
ADMIN_INFO = ("9999999999","admin@digital.com")

# Display System Info 
print("=" * 50)
print(f"        Welcome To {SYSTEM_INFO[0]}")
print(f"        Software {SYSTEM_INFO[1]} - {SYSTEM_INFO[-1]}")
print("=" * 50)

# Core Functionalities (CRUD)
# Add Student -> ID, Name, Scores, Skills
# Add Student -> ID(only one), Name(only one), Scores(Multiple), Skills(Multiple)
# Whole System -> Multiple Students -> Which Data Structure is appropriate ?

# Whole System -> Multiple Students -> Which Data Structure is appropriate -> Dictionary

# students = {
#     "101":{
#         "name":"Ravi",
#         "scores":[90,80,90],
#         "skills":{"python","sql","sql"}
#     },
#     "102":{
#         "name":"Mike",
#         "scores":[90,80],
#         "skills":{"python","sql",}
#     }
# }

students = {}

# Create Student Function 
def add_student():
        # Create Student 
        print("=" * 30)
        print("     Adding Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            print("OOPS! Student ID Already Exists!!!!")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break 
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print("Invalid Score, Score Should be (0-100)")
                else:
                    print("Invalid Score, Only Digits Allowed")
                    
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                else:
                    skills.add(skill_input)
                    
            print(students) # Before Adding
            
            print("========== Student Added ==========")
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            
            print(students) # After Adding

# Update Student Function 
def update_student():
        # Updating Student 
        print("=" * 30)
        print("     Updating Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            new_name = input("Enter New Name: ").title()
            students[student_id]['name'] = new_name
            print("=" * 30)
            print("Student Details Updated")
            print("=" * 30)
        else:
            print("=" * 30)
            print("OOPS!!! Student ID Doesn't Exist")
            print("=" * 30)
        
        print(students) # After Updating             

# Delete Student Function 
def delete_student():
        # Deleting Student 
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            students.pop(student_id)
            print("=" * 30)
            print("Student Record Deleted")
            print("=" * 30)
        else:
            print("=" * 30)
            print("OOPS!!! Student ID Doesn't Exist")
            print("=" * 30)
            
        print(students) # After Deleting 

# Read Student Function 
def read_student():   
    # Reading Student 
        print("=" * 30)
        print("     Reading Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            
            # fetch student details 
            data = students[student_id]
            
            # data = students['101']
            # data = {'name': 'Ravi', 'scores': [90,80], 'skills': {'python'}}
            # {'101': {'name': 'Ravi', 'scores': [90,80], 'skills': {'python'}}}
            name = data['name'] # Ravi
            scores = data['scores'] # 90 
            skills = data['skills'] # python 
            
            # Average Score 
            average_score = sum(scores) / len(scores)
            
            # Highest Score 
            high_score = max(scores) 
                    
            # Lowest Score 
            low_score = min(scores) 
                    
            # Skills Count 
            skills_count = len(skills)
            
            # Displaying All Details 
            print("=" * 30)
            print("     Student Details")
            print("=" * 30)
            print(f"ID: {student_id}")
            print(f"Name: {name}")
            print(f"All Scores: {scores}")
            print(f"Average Score: {average_score}")
            print(f"Highest Score: {high_score}")
            print(f"Lowest Score: {low_score}")
            print(f"All Skills: {skills}")
            print(f"Skills Count: {skills_count}")
            
        else:
            print("=" * 30)
            print("OOPS!!! Student ID Doesn't Exist")
            print("=" * 30) 

# Search Student Function 
def search_student():   
    # Searching Student 
        print("=" * 30)
        print("     Searching Student")
        print("=" * 30)
        
        skill_to_search = input("Enter Skill To Search: ")
        filtered_students = list(filter((lambda student_id: skill_to_search in students[student_id]['skills']), students))
        print(filtered_students) # After Searching 
        
        if filtered_students:
            print("=" * 30)
            print(f"     Student With Skills {skill_to_search}")
            print("=" * 30)
            
            for student_id in filtered_students:
                print(f"Student ID: {student_id} - Student Name {students[student_id]['name']}")
        else:
            print("=" * 30)
            print(f"     Student With Skills {skill_to_search} Not Found")
            print("=" * 30)

# Exit Application Function 
def exit_app():  
    # Exit Application 
        print("=" * 30)
        print("     Exiting Application")
        print("=" * 30)

        # Display Admin Info 
        print("=" * 50)
        print(f"        Admin Contact Number {ADMIN_INFO[0]}")
        print(f"        Admin Email ID {ADMIN_INFO[1]}")
        print("=" * 50)

# Build Menu Based System for CRUD 
while True:
    print("=" * 30)
    print("Choose An Option: ")
    print("=" * 30)
    
    print("1 - Create Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Search Student")
    print("6 - Exit Application")
    
    choice = input("Enter Your Choice (1-6): ")
    
    if choice == "1":
        add_student()
    
    elif choice == "2":
        update_student()
        
    elif choice == "3":
        delete_student()
        
    elif choice == "4":
        read_student()
        
    elif choice == "5":
        search_student()
        
    elif choice == "6":
        exit_app()
        break
        
    else:
        # Invalid Option
        print("=" * 60)
        print("     Invalid Option Selected, Only Select (1-6)")
        print("=" * 60)