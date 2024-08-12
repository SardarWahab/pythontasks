print('Calculate the grade of students')
obtained_marks = int(input('Enter your obtained marks:'))
total = 1100
result = obtained_marks/total*100

if result > 90 and result < 100:
    print('You are in A+ grade')
elif result > 80  and result <89:
    print('You are in A grade')
    
elif result > 70 and result <79:
    print('You are in B+ grade')
elif result > 60 and result <69:
    print('You are in B grade')
elif result > 50 and result <59:
    print('You are in C grade')

else:
 print("mazrat, ap k lowdy lag gaye hain")
    
