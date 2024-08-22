class mobile:
    def __init__(self,name,color,memory):
        self.name = name
        self.color = color
        self.memory = memory
    
    def entred(self):
        return f"The mobile name is {self.name}, the color is {self.color} and the memory is {self.memory}"
    


Tecno = mobile("Tecno",'black','64GB')
print(Tecno.entred())

Infinix = mobile("infinix",'White','128GB')
print(Infinix.entred())
