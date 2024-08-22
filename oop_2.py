class car:
    def __init__(self,name,model,year):
       self.name = name
       self.model = model
       self.year = year
    def start(self):
        return f"my branded car name is:{self.name}"

my_car = car("TYOTA",'HIAS','2023')
# print(my_car.name,my_car.model,my_car.year)


MY_TOYTA = car("Truck","Bredford","1990")
# print(MY_TOYTA.name,MY_TOYTA.model, MY_TOYTA.year)
print(MY_TOYTA.start())