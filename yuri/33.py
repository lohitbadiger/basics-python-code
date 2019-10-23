# global functions in python

name='Yuri'
student='lohit'


def names():
    global student
    name='Lohit Badiger'
    print('the person is ', name)
    
names()    

print('global names are', name)
print('global names are', student)



num1=10
num2=20

def sum():
    
    global num1,num2
    
    print(num1+num2)
 
    
  

sum()