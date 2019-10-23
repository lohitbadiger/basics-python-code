class employee:
    
    def __init__(self,pay,name,age):
        
        self.pay=pay
        self.name=name
        self.age=age

    def fullname(self):
        return '{} {}'.format(self.name,self.age)
    
    
    def salery_hike(self):
        self.pay=int(self.pay*2)


lohit=employee(200,'lohit',20)
print(lohit.pay)

lohit.salery_hike()
print('lohit salary is hiked by',lohit.pay)



yuri=employee(500,'yuri',18)

print(yuri.pay)