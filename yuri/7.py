# Format Method 

#in this method we can print the variables using {}


number1=300.134435
number2=2.3343434 
number3=10.202940
number4=233.378343244234


#1 way

print('lottory number is {0} and second number is {1}'.format(number1,number2))

# for printing the total 4  digits 

print('First number is {0} and second number is {1} and number 3 is {2:.3}'.format(number1,number2,number3))


# for printing 5 float digits 

print('First number is {0:.5f} '.format(number4))


print('-----------------------------------------------------')


# 2nd way 

print(f'the prize number is {number1} {number2} {number3}')
print('-----------------------------------------------------')

print(f'the  second prize number is {number2:.4}')
# Fractional word
print(f'the  second prize number is {number4:.4f}')

