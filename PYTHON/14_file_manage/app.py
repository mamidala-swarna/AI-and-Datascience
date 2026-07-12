# Student Management System -> Using Functional Style -> Use Persistent Storage i.e Save Data To File (JSON)

# Menu Based System -> In Future if you learn full stack, replace menus with UI Elements like Buttons 

# System Setup -> READ Only (Tuple)
SYSTEM_INFO = ("Digital Tech","Student Management System","v1")

# Admin Info -> READ Only (Tuple)
ADMIN_INFO = ("9999999999","admin@digital.com")

# Display System Info 
print("=" * 50)
print(f"        Welcome To {SYSTEM_INFO[0]}")
print(f"        Software {SYSTEM_INFO[1]} - {SYSTEM_INFO[2]}")
print("=" * 50)

# Core Functionalities (CRUD)
# Add Student -> ID, Name, Scores, Skills
# Represent Above Student Details in Dictionary 

# Importing Utilities Needed 
import json,os 

# File To Store Students Data 
FILE_NAME = "14_file_manage/students.json"

# Load Students Data From JSON File
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file_data:
            return json.load(file_data) 
        for sid in data:
            data[sid]["skills"]= set(data[sid]["skills"])

            return data
             
    else:
        return {}

# Save Students Data To JSON File 
def save_students():
    # TypeError: Object of type set is not JSON serializable
    # Fix above issue - convert the Python set into a list 
    json_data_fix = {
        # {'101': {'name': 'Ravi', 'scores': [90], 'skills': {'python'}}}
        sid: {
            "name": data['name'],
            "scores": data['scores'],
            "skills": list(data['skills'])
        }
        for sid, data in students.items()
    }
    
    with open(FILE_NAME,"w") as file_data:
        json.dump(json_data_fix,file_data,indent=4)
        
# Set Students Details In Dictionary
students = load_students()

# Adding Student Function
def add_student():
        # Create / Add Student 
        print("=" * 30)
        print("     Adding Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            print("OOPS! Student ID Already Exists")
        else:
            name = input("Enter Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or Type done: ")
                if score_input == "done":
                    break 
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print("Invalid Score, Score should be (0-100)")
                else:
                    print("Invalid Score, Only Digits Allowed")
                    

            skills = set()
            while True:
                skill_input = input("Enter Skill or Type done: ")
                if skill_input == "done":
                    break
                else:
                    skills.add(skill_input) 
                    
            print(students) # Before Adding 
            print("=========== Student Added ===========")
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            save_students() # Write Data To JSON File
            print(students) # After Adding i.e for confirmation


# Updating Student Function
def update_student():
        # Update Student 
        print("=" * 30)
        print("     Updating Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            new_name = input("Enter Name: ").title()
            students[student_id]['name'] = new_name
            print("=" * 30)
            print("Student Updated")
            print("=" * 30)
        else:
            print("=" * 50)
            print("OOPS! Student ID Doesn't Exists")
            print("=" * 50)
        save_students() # Write Data To JSON File
        print(students) # After Updating i.e for confirmation


# Deleting Student Function
def delete_student(): 
        # Delete Student 
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        if student_id in students:
            students.pop(student_id)
            print("=" * 30)
            print("Student Deleted")
            print("=" * 30)
        else:
            print("=" * 50)
            print("OOPS! Student ID Doesn't Exists")
            print("=" * 50)
        save_students() # Write Data To JSON File
        print(students) # After Deleting i.e for confirmation   
    
# Reading Student Function
def read_student(): 
        # Read Students 
        print("=" * 30)
        print("     Reading Student")
        print("=" * 30)
        
        student_id = input("Enter ID: ")
        
        if student_id in students:
            
                # Fetch specific student data
                data = students[student_id]
        
        
                # id is already fetched i.e sid 
                # fetch name, scores, skills etc 
                name = data['name']
                scores = data['scores'] # All Scores
                skills = data['skills'] # All Skills 
                
                # Average Score 
                scores = data["scores"]

                total_score = 0
                count_scores = 0

                for score in scores:
                    total_score += score
                    count_scores += 1

                if count_scores > 0:
                   avg_score = total_score / count_scores
                else:
                   avg_score = 0
                
                # Highest Score
                if scores:
                     high_score = max(scores)
                     low_score = min(scores)
                else:
                    high_score = 0
                    low_score = 0
                
                for score in scores:
                    if score < low_score:
                        low_score = score
                
                
                # Skills Count 
                skill_count = 0
                for skill in skills:
                    skill_count += 1
                
                # Displaying Student Information
                print("=" * 30)
                print("     Student Information")
                print("=" * 30)
                print(f"ID: {student_id}")
                print(f"Name: {name}")
                print(f"All Scores: {scores}")
                print(f"Average Score: {avg_score}")
                print(f"Highest Score: {high_score}")
                print(f"Lowest Score: {low_score}")
                print(f"All Skills: {skills}")
                print(f"Skills Count: {skill_count}")
                print("=" * 30)
        
        else:
            print("=" * 50)
            print("OOPS! Student ID Doesn't Exist")
            print("=" * 50)

# Searching Student Function   
def search_student():
        # Searching Students 
        print("=" * 30)
        print("     Searching Student")
        print("=" * 30)
        
        skill_to_search = input("Enter Skill To Search: ")
        # list(filter((lambda product: product['price'] > 25000), products))
        filtered_students = list(filter((lambda student_id: skill_to_search in students[student_id]['skills']), students))
        print(filtered_students) # After Filtering i.e for confirmation   
        
        if filtered_students:
            print("=" * 30)
            print(f"     Students With Skills {skill_to_search}")
            print("=" * 30)
            
            for student_id in filtered_students:
                print(f"Student ID: {student_id} - Student Name {students[student_id]['name']}")
        else:
            print("=" * 30)
            print(f"     Students With Skills {skill_to_search} Not Found")
            print("=" * 30)


# Exiting Application Function   
def exit_app():
    # Exit Application
        print("=" * 50)
        print("     Exiting Application")
        print("=" * 50)
        print(f"        Admin Contact Number {ADMIN_INFO[0]}")
        print(f"        Admin Email ID  {ADMIN_INFO[1]}")
                

# Build Menu Based System for different (CRUD) operations 
while True:
    print("Choose An Option: ")
    print("1 - Create student") # Write Data To File 
    print("2 - Update student") # Write Data To File 
    print("3 - Delete student") # Write Data To File  
    print("4 - Read students")  # Read Data From File  
    print("5 - Search students") # Read Data From File  
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
        # Invalid Choice
        print("=" * 50)
        print("     Invalid Option, Only Use (1-6)")
        print("=" * 50)
        
    
    
    