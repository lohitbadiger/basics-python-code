class employee:
    
    increased=2
    addd=0
    def __init__(self,name,age,pay):
        self.name=name
        self.age=age
        self.pay=pay
        employee.addd+=1
    
    def fullname(self):
        return '{} {} '.format(self.name,self.age,self.pay)
    

    def salery_hike(self):
        self.pay=int(self.pay* employee.increased)
   
lohit=employee('lohit',20,2000)

yuri=employee('yuri', 20,4000)

yurid=employee('yuri', 20,4000)


print(lohit.pay)

lohit.salery_hike()
print(lohit.pay)



lohit.increased=10
lohit.salery_hike()

print(lohit.pay)

print(lohit.__dict__)

print(employee.addd)