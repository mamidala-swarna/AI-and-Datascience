#File Management Using Python
# Syntax - 1
# file = open("file_path","mode")

#file_data=open("14_file_manage/filenew.txt","r") # FileNotFoundError: [Errno 2] No such file or directory: '14_file_manage/filenew.txt'
file_data=open("file.txt","r")

print(file_data)

print(file_data.closed) # False -> File is open
print(file_data.close())#Closes the file
print(file_data.closed)#True->File  is closed

# Syntax - 2 (Recommended)
# with open("file_path","mode") as alias_name:

with open("file.txt","r") as file_data:
    print(file_data)
print(file_data.closed) # True --> Now Closed Automatically 

print("=" * 50)

#Read Whole Data
with open("file.txt","r") as file_data:
    print(file_data.read())

print("=" * 50)

#Read Data Character wise
with open("file.txt","r") as file_data:
    for character in file_data.read():
        print(character)

print("=" * 50)

#Read Data Word wise
with open("file.txt","r") as file_data:
    for word in file_data.read().split():
        print(word)

print("=" * 50)

#Read Data First Line
with open("file.txt","r") as file_data:
    print(file_data.readline())
print("=" * 50)

#Read Data Multiple Lines
with open("file.txt","r") as file_data:
    print(file_data.readlines())

print("=" * 50)

#Read Data Multiple Line with line wise
with open("file.txt","r") as file_data:
    for line in file_data.readlines():
        print(line.strip())

print("=" * 50)
#Earlier we created file manually

#now we use python to create file
with open("write.txt","w") as file_data:
    print(file_data)

print("=" * 50)

#Now we use python to write data to file
with open("write.txt","w") as file_data:
    file_data.write("Heyy Whatsupp !!")

print("=" * 50)

#Now we use pyhton to write data to file using Append mode
with open("write.txt","a") as file_data:
    file_data.write("  How had you been?")

print("=" * 50)

#Now use python to write data file using Appwnd Mode
with open("write.txt","a") as file_data:
    file_data.write(" I'm doing well")

print("=" * 50)

#Folders/Directory Management
#directory_name="14_file_manage/students_data"

import os
directory_name="students_data"

import os

directory_name = "students_data"

if os.path.exists(directory_name):
    print("The folder already exists.")
else:
    os.mkdir(directory_name)
    print("Folder created successfully.")

#Delete Empty Folder
os.rmdir(directory_name)

#Delete File
if os.path.exists("text.txt"):
    os.remove("text.txt")
