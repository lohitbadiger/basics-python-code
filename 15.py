# def area(radius):
#     print(3.142* radius * radius)


# area(4)


# Pass by Reference
# Here x is a new reference to same list lst 


# def myFun(x): 
#     x[0] = 20

# # Driver Code (Note that lst is modified 
# # after function call. 
# lst = [10, 11, 12, 13, 14, 15] 
# myFun(lst)
# print(lst)
 
print('_____________________link broken___________________________________')

# def myFun2(x): 
#    x[0] = 120
#    x[1] = 12000090
   
    
#    xss = [20, 30, 40] 
   
#    # After below line link of x with previous 
#    # object gets broken. A new object is assigned 
#    # to x. 
  
# # Driver Code (Note that lst is not modified 
# # after function call. 
# lst = [10, 11, 12, 13, 14, 15,73847,2347234]  
# myFun2(lst); 
# print(lst)

# def myFun(x): 
  
#    # After below line link of x with previous 
#    # object gets broken. A new object is assigned 
#    # to x. 
#    x = 20
  
# # Driver Code (Note that lst is not modified 
# # after function call. 
# x = 10 
# myFun(x); 
# print(x)  
# (x)  

# print('---------------------------------')
# print()


# # Python program to illustrate   
# # *args for variable number of arguments 
# def myFuns(*argv):  
#     for arg in argv:  
#         print (arg) 
    
# myFuns('Hello', 'Welcome', 'to', 'spcieup ','hsdjsdjhfds',233)  




# def area(radius):
#     print(3.142* radius * radius)


# area(4)




# def area(radius):
#     return 3.142 * radius * radius
    

# def volume(area,length):
#         print(area * length)


# radius=int(input('enter the value for the radius'))
# length=int(input('enter the value of length ' ))


# volume(area(radius), length)




def lohit(dictionary):
    for key, val in dictionary.items():

        print(f'I know this  a {key} programing and this is  {val}, a framework of {key}')

lohit_items= {}

while True:
    lohit_program= input('enter name of programming ')
    lohit_frame=input('enter the name of frame work ')
    lohit_items[lohit_program]=[lohit_frame]

    another=input('add another program? (y/n)')
    if another=='y': 
        continue
    else:
        break

lohit(lohit_items)



