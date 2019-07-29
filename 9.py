# identity


x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3,4]
y3 = [1,2,3,4]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is not y3)
print('-------------------------------------------------------')


# Logical 
x = False
y = False

# Output: x and y is False
print('x and y is',x and y)

# Output: x or y is True
print('x or y is',x or y)

# Output: not x is False
print('not x is',not x)


print('-------------------------------------------------------')
print('-------------------------------------------------------')

# _membership.
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y) 
print('------------------------------------------')
# today='monday'
today='sunday'


yoga_day='monday'

print(today is yoga_day)