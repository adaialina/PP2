fruits = ['apple', 'orange', 'banana', 'pear']
a = open('newlist.txt', 'w')
for i in fruits:
    a.write('\n'+i)

a.close()