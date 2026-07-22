# With Inheritance - We Don't Need To Same Functionalities again and again multiple times 
# LMS Application (Application For Watching Course Videos)
# Student       ->  Watch Videos 
# VideoAdmin    ->  Watch Videos & Add Videos  
# SuperAdmin    ->  Watch Videos, Add Videos & Delete Videos 
class Student:
    #watch videos
    def watch_videos(self):
        print("=" * 50)
        print("Functionality For Watching Videos")
        print("=" * 50)
        print("W")
        print("A")
        print("T")
        print("C")
        print("H")
        print("I")
        print("N")
        print("G")
        print("V")
        print("I")
        print("D")
        print("E")
        print("O")
        print(".............")# real world code is say 2000 lines of code 

class VideoAdmin(Student):
    #Add Videos
    def add_videos(self):
        print("=" * 50)
        print("Functionality For  Adding Videos")
        print("=" * 50)
        print("A")
        print("D")
        print("D")
        print("I")
        print("N")
        print("G")
        print("V")
        print("I")
        print("D")
        print("E")
        print("O")
        print("..............") # real world code is say 2000 lines of code

class SuperAdmin(VideoAdmin):
    # Deleting Videos
    def delete_videos(self):
        print("=" * 50)
        print("Functionality For Deleting Videos")
        print("=" * 50)
        print("D")
        print("E")
        print("L")
        print("E")
        print("T")
        print("I")
        print("N")
        print("G")
        print("V")
        print("I")
        print("D")
        print("E")
        print("O")
        print("..............") # real world code is say 2000 lines of code
        
    # Now Technically we have eliminated 6000 Lines Of Duplicate Code 
print("Student User")
student_user=Student()
student_user.watch_videos()

print("Video Admin User")
video_admin_user=VideoAdmin()
video_admin_user.watch_videos()
video_admin_user.add_videos()

print("Super Admin User")
super_admin_user=SuperAdmin()
super_admin_user.watch_videos()
super_admin_user.add_videos()
super_admin_user.delete_videos()
