# def square(n):
#     ''' Take in number n, return the square of n'''
#     print(n**2)
    
# square(5)
# print(square.__doc__)
     

    #  new
def factorial(n):
    if(n==0 or n  ==1):
     return 1
    else:
       return n* factorial(n-1)
    
print("The factorial ",factorial(2))    
print("The factorial ",factorial(3))
print("The factorial ",factorial(4))        