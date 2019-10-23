class planet:
    
    
    shape='sqaure'
    
    def __init__(self, water, moon):
        self.water=water
        self.moon=moon
        
    
    def orbit(self):
        return f'{self.water} and satellite is {self.moon}'
    
    
    @classmethod
    def commons(cls):
        return f'all the palnets are {cls.shape}'
    
naboo=planet('yes', 'moon is not prsent')

print(planet.shape)
    
print(planet.commons())   


        
        