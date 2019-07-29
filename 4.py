list=('lohit',2,3,4)

print(list)

print(list[0])
print(list[2])

# list[2]=7    #error bcz immutable value cannot be changed

print(list[2])

# An empty tuple 
empty_tuple = () 
print (empty_tuple) 


# Creating non-empty tuples 

# One way of creation 
tup = 'python', 'geeks'
print(tup) 

# Another for doing the same 
tup = ('python', 'geeks') 
print(tup) 


# Code for concatenating 2 tuples 

tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 

# Concatenating above two 
print(tuple1 + tuple2) 

# Code for creating nested tuples 

tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 
tuple4 = (0, 1, 2, 3) 

tuple3 = (tuple1, tuple2,tuple4) 
print(tuple3) 

# Finding Length of a Tuple
tup=('python','php','sfgkdfjkghd')
print(len(tup))


tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)           # Prints complete list
print (tuple[0])        # Prints first element of the list
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:] )      # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints list two times
print (tuple + tinytuple) # Prints concatenated lists