# #the argument name is the required argument to the function func   
# def func(name):  
#     message = "Hi "+name;  
#     return message  
# name = input("Enter the name?")  
# print(func(name))  

# scope variable 



def print_message():  
    message = "hello !! I am going to print a message." # the variable message is local to the function itself  
    return message
print_message()  
print(print_message()) # this will cause an error since a local variable cannot be accessible here.   