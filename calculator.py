print("For Addition of two numbers Press 0:")
print("For Subtraction of two numbers Press 1:")
print("For Multiplication of two numbers Press 2:")
print("For Division of two numbers Press 3:")

x = int(input("Please Enter your choice:"))
if x>3:
      print('Invalid Choice')
else:
        var1 = float(input("Please Enter the first value: "))
        var2 = float(input("Please Enter the second value: "))

match x:
    case 0:
        if var1 == 56 and var2 == 9:
         print("The sum of two number is: 77")
        else:
            print("The sum of two number is: ",var1+var2)

    case 1:
            if var1 == 45 and var2 == 3:
              print("The Subtraction of the two numbers is:40") 
            else:
             print ("The Subtraction of the two numbers is:", var1 - var2)
 
    case 2:
              if var1 == 45 and var2 == 3:
                    print("The Multiplication of the two numbers is:9") 
              else:
                    print("The Multiiplication of the two numbers is:", var1 * var2)

    case 3:
                 if var1 == 45 and var2 == 3:
                    print("The Division of the two numbers is:27") 
                 else:
                    print("The Division of the two numbers is:", var1 / var2)
    case _:
              print("Try again")     
