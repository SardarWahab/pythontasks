# f = open('m.txt','r')
# text = f.read()
# print(text)
# f.close
               # new
f = open('f.txt','w')
f.write("Hallo Wahab")
# print(text)
# f.close
with open('f.txt', 'a') as f :
    f.write("Han Bahi kon sa  chaker ma ha ")