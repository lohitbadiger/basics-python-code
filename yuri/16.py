food=input("do you eat meat? xyz: ")

if food!='yes':
    print('Im a non-veg')

else:
    print('vegetarian')
    


# #operater
# #   < , > ,== , <=, !=

food=input('do you eat food (y/n):')
if food!='tasty':
    print('food is not tasty')
else:
    print('food is very taste')
    
    
x=20
 
if x < 50 :
    print('(first suite)')
    print('x is small')
    print('x is small')
    

else:
    print('(second suite)')
    print('x is large')


age = int (input("Enter your age? "))  
if age>=18:  
    print("You are eligible to vote !!");  
else:  
    print("Sorry! you have to wait !!"); 
    

name='rekha'

if name=='lohit':
    print('hii lohit')

elif name=='manoj':
    print('hii manoj')

elif name=='rekha':
    print('hii rekha')

else:
    print('hii welcome to all')
    

marks = int(input("Enter the marks? "))  
if marks > 85 and marks <= 100:  
   print("Congrats ! you scored grade A ...")  
elif marks > 60 and marks <= 85:  
   print("You scored grade B + ...")  
elif marks > 40 and marks <= 60:  
   print("You scored grade B ...")  
elif (marks > 30 and marks <= 40):  
   print("You scored grade C ...")  
else:  
   print("Sorry you are fail ?")  