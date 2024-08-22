class BS:
    def __init__(self,Name,Roll_No,Session) :
        self.Std_name = Name
        self.Roll_No = Roll_No
        self.Session = Session
    def bring(self):
        return f"The student name is {self.Std_name} student Roll No is {self.Roll_No} and student session is {self.Session}"
    


std1 = BS('Bazer','12','2020-2024')
print(std1.bring())