def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * fact(n-1)
    
a = int(input("Enter a number that you find factorial:"))
f = fact(a)
print(f"The factorial of {a} is {f}")