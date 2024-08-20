def check_num(inp):
    if inp % 2 == 0:
        return "The Entered number is Even"
    else:
        return "The Entered number is Odd"
    
a = check_num(int(input("Please Enter a number")))
print(a)
      