# def square(n):
#     return n**2

# b= int(input("Please Enter a number:"))
# a = square(b)
# print(f"The Square of {b} is  {a}")


# def ad(*num):
#     return sum(num)
   
# a = ad(11,12)
# print(a)  # Output: 23
import random

jokes = ["Hee", "Hahahaha", "Hi, Today I'm your instructor"]



def get_joke(jokes):
    rand = random.randrange(0,3)
    

    print(jokes[rand])

get_joke(jokes)