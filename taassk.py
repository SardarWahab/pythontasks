#Sum of all number in the llist


numbers = [10, 20, 30, 40, 50]
s = 0
for number in numbers:
    s += number  
print(f"The sum of all elements in the list is:{s}")


#Chracter of string 

# nst = 'Abdul_Wahab_Kashmiri'
# for ind in nst:
#     print(ind[0])



#Take start and end point 

start = int(input("Enter the start point: "))
end = int(input("Enter the end point: "))

numbers = []

for num in range(start, end):
    numbers.append(num) 
print(f"The list of numbers between {start} and {end} is: {numbers}")


