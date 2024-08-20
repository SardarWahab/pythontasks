def grade_s(num1,num2,num3,num4):
    num = num1+num2+num3+num4
    print(f"The sum of all marks are{num}")
    if num >= 90:
        return "A+"
    elif num >= 80:
        return "A"
    elif num >= 70:
        return "B+"
    elif num >= 60:
        return "B"
    elif num >= 50:
        return "C"
    else:
        return "F"
    
std1 = [20,50,30,60]
a = grade_s(20,50,30,60)
print(a)
    
    

