condition = True
st =[]
while condition == True:
   std = input("Enter a string: ")
   st.append(std)
   ch = input("Do you want to continue? (yes/no): ")
   if ch.lower() == "no":
        condition = False
        
print(st)

    
