# # simple function define

# def greet():
#     print("helllo world and Nae is my new student")
    
# greet()
# greet()
# greet()
# greet()
# greet()
# greet()
# greet()
# greet()

# fun with parameter//arguments passing

# def greet(name,time,program):
#     print(f'Hello {name} what are you doing at this {time} time')
#     print('Hello', name , 'what are you doing at this',time )

#     print( name ,time,program )

# greet('lohit','marnig', 'Python')



# arguments passing by user by input 
# def greet(name,time):
#     print(f'good morning{name}, hope your greate at this {time}')


# xyz = input('enter your name')
# yzw = input('enter the time')

# greet(xyz, yzw)

# functions with default values 

def greet(name="ryu" , time="morning"):
    print(f'Good morning {name} , what are you doing in the {time}')
    
 #its going to print name= ryu and time="mornig"
# greet()
print('------------------------------------------------------------')

#override the name nd time here??
greet("lohit", "assadsasd") 
print('------------------------------------------------------------')

greet("rek", "assafsfsddsasd") #override the name nd time here??

print('------------------------------------------------------------')

greet("sfdfdsfdloht", "fsfdassadsasd") #override the name nd time here??

print('------------------------------------------------------------')

greet()



# Python program to demonstrate 
# default arguments 
def myFun(x, y=50): 
    print("x: ", x) 
    print("y: ", y) 
  
# Driver code (We call myFun() with only 
# argument) 
myFun(10) 
myFun(10,343)
myFun(10,343) 
myFun(10,343) 
myFun(10,343) 
 
