num = int(input('Please Enter a number:'))
for i in range (0,20):  
  if i % 5 == 0:
    print("It is divisibe by 5")  
    continue  
  print(f"{num} x {i} = {num*i}")


