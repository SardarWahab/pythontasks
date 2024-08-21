# def personal(*rec):
#     return 


# my_dic = ('Ahmad',40,'Mandhole poonch')
# a = personal(*my_dic)
# print(a)

def personal(*rec):
   
    total =0
    for i in rec:
     total += i
     length  = len(rec)
     avg = total/length
     return f" The sum is:{total}"
     print(total/avg)
     return sum(rec)


a = personal(1,2,3,4)
print(a)



    