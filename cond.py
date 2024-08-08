print('Conditional Statement')
student = ['Ahmad','Usman','Bazar','Saran']
name = input('Please Enter name that you find:')
if name in student:
    print(student.index(name))
else:
     print(student.append(name))

print(student)