class Future:
    
    fun='very happy'
        #creating a class level object
    def __init__(self,name,age,game,system):
        self.name=name
        self.age=age
        self.game=game
        self.system=system
        
        
    def orbit(self):
        return f'{self.name} is ---->{self.age}'
    
    
instance=Future('lohit',20,'baseball','linear - system')


print(f'Name is :{instance.name}')

print(f'age is :{instance.age}')
print(f'game is :{instance.game}')
print(f'system is :{instance.system}')


# im writing "class_name".'variable_name'
print(Future.fun)


# im writing "instance".'variable_name'

print(instance.fun)