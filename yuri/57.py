
class Person2:
    
    # property that person will contain
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person2("John", 36)

# to delete an argument from class

del p1.age

print(p1.age)
