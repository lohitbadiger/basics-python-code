# Variable length arguments:
# We can have both normal and keyword variable number of arguments. Please see this for details.


# Python program to illustrate   
# *args for variable number of arguments 

def address(*argv):
    for arg in argv:
        print(arg)
        

address('lohit','hubli',89898993,"389HJsdhf")

address('lohit','jdskflslkfdsldf','hubli',89898993,"389HJsdhf",'dshkfhksfd','kajfsljfdl')

        
    
    