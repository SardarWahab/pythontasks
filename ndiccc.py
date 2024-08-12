print('Calculate the grade of students')
# grade = int(input('Please Enter Your Grade'))
obt = int(input('Enter your obtained mark:'))
total = 1100
res = obt/total*100

if res > 90 and res< 100:
    print('You are in A+ grade')
elif res > 80  and res <90:
    print('You are in A grade')
    
elif res > 70 and res <80:
    print('You are in B+ grade')
elif res > 60 and res<70:
    print('You are in B grade')
elif res > 50 and res<60:
    print('You are in C grade')

else:
 print("Congrats lora lag ga........")
    
