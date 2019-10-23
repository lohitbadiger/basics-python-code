# height=int(input('enter The value for base,Hight :'))
# base=int(input('netre valeu '))


# print(base,height)
# print('-----------------------------')
# area=0.5*int(base*height)
# print(area)


# Tuplessssssssssssss

list=(1,2,3,4)

print(list)

# # non mutable or not  changable
# list[2]='jsdfk'
# print(list)



empty_tuple=()
print(empty_tuple)



# One way of creation 
# Creating non-empty tuples 

tuple='python', 'Yuri'
print(tuple)

# Another for doing the same 

tuple=('python', 'Yuri')
print(tuple)

print('-----------------------------------')

yri=(1,2,4,5)
add=('python','Geetksjhd')
print(yri+add)


print('-----------------------------------')
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 
tuple3 = (tuple1, tuple2) 
print(tuple3) 



# Finding Length of a Tuple
tup=('python','php','fdks')
print(len(tup))

print('-------------------------------------------')
tupyuri=('asndassndjsa')
print(len(tupyuri))
print('-------------------------------------------')



my_tuple = ('p','e','r','m','i','t')

print(my_tuple[0])   # 'p' 
print(my_tuple[5])   # 't'

print('-------------------------------------------')


n_tuple = ("mouse lohit", [8, 4, 6], (1, 2, 3,'Yuri'))

# nested index
print(n_tuple[0][6:12])       

print('-------------------------------------------')

print(n_tuple[0][6])       

print('-------------------------------------------')

print(n_tuple[1][1]) 
print('-------------------------------------------')

print(n_tuple[2][3]) 

print('-------------------------------------------')

my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple[:-8])
print('-------------------------------------------')

print(my_tuple[2:-6])

del n_tuple
# print(n_tuple)


multiple=(1,2,3)
print(multiple*3)


print('-------------------------------------------')

my_tuple = ('a','p','p','l','e',)

# In operation
# Output: True
print('a' in my_tuple)

# Output: False
print('b' in my_tuple)

# Not in operation
# Output: True
print('g' not in my_tuple)


for name in ('John','Kate'):
     print("Hello",name)    