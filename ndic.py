print('Conditional Statement')
indic= []
outdic = []
book = {
     'chita':'white',
     'kala':'Black',
     'nela':'Blue',
     'wahab':'Peroo',
     'ifraheem': 'Han g chita g',
     'kafeel':'noughty boy',
     'Ayaz':'Babu bhiya',
     'saran':'Utha la ra diwa or ptak da Euorep ma',
     'haider':'Molvi tabha da ',
     'shahel':'Youthiya',
     'frahad':'Baba g dam kar dyo',
     'bilal':'Nosra',
     'alyan':'Tharki',
     'arslan':'G thk',
     'sameer':'Makeup',
     'usman':'Basheer',
     'zeshan':'Raja g',
     'moneeb':'Baber Azam'
}
name = input('Please Enter name that you find and input must be in niki abc:')
if name in book:
    print(f'its mean {name}.The meaning of {name} is {book.get(name)}' )
    indic.append(name)
    print(f'The indic words list:{indic}')
else:
     print(f'No,{name} is not found')
     outdic.append(name)
     print(f'The outdic words list:{outdic}')



     

