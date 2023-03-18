import os 

print('1st Test:', 'alina.txt')
print('Existence:', os.access('alina.txt', os.F_OK))
print('Readability:', os.access('alina.txt', os.R_OK))
print('Writability:', os.access('alina.txt', os.W_OK))
print('Executability:', os.access('alina.txt', os.X_OK))