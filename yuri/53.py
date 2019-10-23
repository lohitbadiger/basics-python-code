class Person1:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person1("John", 36)
p1.myfunc()



class soemthing:
    
    def __init__(ok,name,age):
        ok.names=name
        ok.age=age
    
    
    def myfunc(abc):
        print("Hello my name is " + abc.names) 
    
    
xyz=soemthing('lohir',200)

xyz.myfunc()





class cars():
    
    def __init__(yuri,name,sea):
        
        yuri.name=name
        yuri.sea=sea
        
    def river(word):
        
        print('im printing the word',word.name)
        
xyz=cars('Yama','South Sea')
xyz.river()      
        
        