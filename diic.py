# dic ={ "wahab":"name",
#         "cup": " Object"
#        }
# print(dic["wahab"])
# print(dic.keys())

# for key in dic.keys:
#     print(dic[key])


    #   new  
# dic = {
#     "wahab": "name",
#     "cup": "Object"
# }

# print(dic["wahab"])
# print(dic.keys())

# for key in dic:
#     print(dic[key])

# new 
ep1 = { 1:200, 2: 344, 4: 533 ,5:500}
ep2 =  {6: 435, 7:345, 8:354}
ep1.update(ep2)
# ep1.clear()
ep1.pop(2)
ep1.popitem()
del ep1[4]
print(ep1)