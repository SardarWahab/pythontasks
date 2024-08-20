def grade_s(std_marks):
    total = 400
    obtain_m = sum(std_marks)
    print(obtain_m)
    obtain_per = obtain_m/total*100
    print(f"The percentage of all marks are{obtain_per}")
    if obtain_per >= 90:
        return "A+"
    elif obtain_per >= 80:
        return "A"
    elif obtain_per >= 70:
        return "B+"
    elif obtain_per >= 60:
        return "B"
    elif obtain_per >= 50:
        return "C"
    else:
        return "F"
    
std1 = [20,50,30,60]
 
print(grade_s(std1))
    
    

