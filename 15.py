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

def myFun2(x): 
   
   # x[0] = 120
   # After below line link of x with previous 
   # object gets broken. A new object is assigned 
   # to x. 
   x = [20, 30, 40] 
  
# Driver Code (Note that lst is not modified 
# after function call. 
lst = [10, 11, 12, 13, 14, 15]  
myFun2(lst); 
print(lst)