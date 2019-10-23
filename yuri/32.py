def area(radius):
    return 3.143*radius*radius


def volume(area, length):
    
    print(area*length)
    
    
radius  =int(input('Enter the number for radius'))

length=int(input('enter the value for length'))

volume(area(radius),length)