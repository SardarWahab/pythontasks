def add(*num):
    return sum(num)

def sub(*num):
    if len(num) < 2:
        return "Error: Not enough arguments"
    else:
        return num[0] - num[1]
    

def mul(*num):
    return num[0] * num[1]

def dvide(*num):
    if len(num) < 2:
        return "Error: Not enough arguments"
    elif num[1] == 0:
        return "Error: Division by zero is not allowed"
    else:
        return num[0] / num[1]
    