# Example: Counting the number of objects of a class
class Student:  
    count = 0  
    def __init__(self):  
        Student.count = Student.count +1
s2=Student()  
s3=Student()  
s4=Student()  

print("The number of students:",Student.count)   
