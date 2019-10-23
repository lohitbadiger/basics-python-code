
# name = input("What is your name: ")
# age = int(input("How old are you: "))
# year = str((2014 - age)+100)
# print(name + " will be 100 years old in the year " + year)

# # define the functin 


# def change_list(list1):
#     list1[0]=100
#     list1.append(70)
#     print("list inside function =", list1)
    

# #defining the list  

# list1=[10,20,30,40,50]

# #calling the function   

# change_list(list1)

# print('list outside function ', list1)



def myFun(x): 
  
   # After below line link of x with previous 
   # object gets broken. A new object is assigned 
   # to x. 
   x = 20
  
# Driver Code (Note that x is not modified 
# after function call. 
x = 10 
myFun(x); 
print(x)  

#defining the function  
def change_string (str):  
    str = str + " Hows you?";  
    print("printing the string inside function :",str);  
  
string1 = "Hi I am lohith"  
  
#calling the function  
change_string(string1)  
  
print("printing the string outside function :",string1)   