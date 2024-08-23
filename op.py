class BS:
    def __init__(self,name, clas , address) :
        self.Fname = name
        self.Class = clas
        self.Address = address

    def meth(self):
        return f"student name is {self.Fname} his class is {self.Class} and his address is {self.Address}"
    


rec = BS('Wahab','BSSE','Mandhole Poonch')
print(rec.meth())
