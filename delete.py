




# x=lambda a:10+a
# print(x(10))

# print('_____________________________')


# x=lambda x,y:x**y
# print(x(5,2))

# print('_____________________________')


# x = lambda ac : ac + 10
# print(x(5))

# print('_____________________________')

# a=lambda x,y,z : x+y+z

# print(a(10,20,30))



# def myfunx(n):
#     return lambda a:a*n

# double=myfunx(3)
# print(double(11))





class father:
    def singer(self):
        print('father can sing')
        
        
        
class son(father):
    def lohit(self):
        print('lohit can do coding')
        

class my_son(son):
    def suss(self):
        print('my son can do dance')
        
       
family=my_son()

family.singer()
family.suss()
family.lohit()

# for instance 'lohit' WANTS TO save ur properties/function of son

lohit=son()        
any_name=son()