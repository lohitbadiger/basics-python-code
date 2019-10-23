# list comprehensions 

# normal way to get output 



# List Comprehensions


numbers=[2,3,4,5,5,7,7]

double=[]
for number in numbers:
    double.append(number*2)
    
    
print(double)

double.append(number*2 for number in numbers)
print('thih is comp way',double)

